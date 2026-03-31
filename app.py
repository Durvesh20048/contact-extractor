from flask import Flask, render_template, request
import re
import spacy
import pdfplumber
import docx

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")


# ---------- TEXT EXTRACTION ----------
def extract_text(file):
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return " ".join([page.extract_text() or "" for page in pdf.pages])

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])

    else:
        return file.read().decode("utf-8")


# ---------- INFO EXTRACTION ----------
def extract_info(text):

    # ---------- EMAIL ----------
    email = list(set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)))

    # ---------- LINKS ----------
    links = re.findall(r"https?://\S+|www\.\S+|linkedin\.com/\S+|github\.com/\S+", text)
    links = list(set(links))

    # ---------- PHONE ----------
    phone = list(set(re.findall(r"(?:\+91[\-\s]?|0)?[6-9]\d{9}", text)))

    # ---------- NAME (RULE BASED) ----------
    lines = text.split("\n")
    possible_name = None

    for line in lines[:5]:
        line = line.strip()
        if line.isupper() and 1 < len(line.split()) <= 3:
            possible_name = line.title()
            break

    # ---------- NLP ----------
    doc = nlp(text)
    # ---------- NAME FROM SENTENCE PATTERN ----------
    pattern_names = []

# pattern like "my name is X"
    matches1 = re.findall(r"my name is ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)", text, re.I)

# pattern like "this is X"
    matches2 = re.findall(r"this is ([A-Z][a-z]+)", text, re.I)

    pattern_names.extend(matches1)
    pattern_names.extend(matches2)

    
    # ---------- LOCATION (NER BASED CLEAN) ----------
    locations = []
    locations = locations[:3]

    for ent in doc.ents:
     if ent.label_ in ["GPE", "LOC"]:
        loc = ent.text.strip()

        # remove unwanted characters
        loc = loc.replace("\n", " ").replace("\r", " ")
        loc = loc.strip()

        # avoid very small or junk values
        if len(loc) > 2:
            locations.append(loc)

# remove duplicates
    locations = list(set(locations))
    # ---------- NAME (NER) ----------
    names = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text.strip())

    names = list(set(names))

    # ---------- CLEAN NAMES ----------
    cleaned_names = []
    for name in names:
        name = name.replace("Email", "").replace("Phone", "")
        name = name.replace("\n", " ").replace("\r", " ")
        name = re.sub(r"\S+@\S+", "", name)
        name = re.sub(r"\d+", "", name)
        name = re.sub(r"[-:]", "", name)
        name = " ".join(name.split())

        if 1 < len(name.split()) <= 3:
            cleaned_names.append(name)

    cleaned_names = list(set(cleaned_names))

    # FINAL NAME
    if possible_name:
     final_name = [possible_name]
    elif pattern_names:
     final_name = list(set(pattern_names))
    else:
     final_name = cleaned_names

    return {
        "name": final_name,
        "email": email,
        "phone": phone,
        "location": locations,
        "links": links,
    }

# ---------- ROUTE ----------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files.get("file")

        if not file:
            return "No file uploaded"

        allowed = (".pdf", ".docx", ".txt")

        if not file.filename.lower().endswith(allowed):
            return "Invalid file type"

        text = extract_text(file)
        result = extract_info(text)

    return render_template("index.html", result=result)


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)