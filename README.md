# 📇 Contact Information Extraction System using NLP
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Information%20Extraction-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/contact-extractor?style=social">
  <img src="https://img.shields.io/github/forks/YOUR_USERNAME/contact-extractor?style=social">
  <img src="https://img.shields.io/github/issues/YOUR_USERNAME/contact-extractor">
  <img src="https://img.shields.io/github/last-commit/YOUR_USERNAME/contact-extractor">
</p>

> **An intelligent NLP-powered application that automatically extracts contact information from unstructured documents such as resumes, emails, chat conversations, and text files.**
>
> **Built using Python, Flask, spaCy NER, and Regular Expressions, the system converts raw text into structured contact details with high accuracy through a hybrid information extraction approach.**
>
> **Supports multiple document formats (PDF, DOCX, TXT) with a modern responsive web interface and is deployable on cloud platforms.**

---

# 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [✨ Features](#-features)
- [🧠 NLP Techniques Used](#-nlp-techniques-used)
  - [Named Entity Recognition (NER)](#1-named-entity-recognition-ner)
  - [Regular Expressions (Regex)](#2-regular-expressions-regex)
  - [Rule-Based Extraction](#3-rule-based-extraction)
- [🛠 Tech Stack](#-tech-stack)
- [📂 Supported Input Formats](#-supported-input-formats)
- [📤 Output](#-output)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [📚 Libraries Used](#-libraries-used)
- [🧪 Test Cases](#-test-cases)
- [🚀 Future Enhancements](#-future-enhancements)
- [🎓 Academic Relevance](#-academic-relevance)
- [📖 Resources & References](#-resources--references)
- [👨‍💻 Developed By](#-developed-by)

---

## 📌 Project Overview

The **Contact Information Extraction System** is a Natural Language Processing (NLP) based web application developed to automatically identify and extract important contact details from unstructured documents.

Traditional documents like resumes, emails, chat logs, introduction paragraphs, and text files usually contain valuable information hidden inside free-flowing text. Manually finding and organizing this information is time-consuming and error-prone.

This application automates that entire process by intelligently extracting:

- 👤 Person Name
- 📧 Email Address
- 📱 Phone Number
- 📍 Location
- 🔗 Website / Portfolio / LinkedIn / GitHub Links

using a combination of **Named Entity Recognition (NER)** and **Regular Expressions (Regex)**.

---

# 🎯 Objectives

- Extract contact information automatically.
- Handle unstructured textual data efficiently.
- Reduce manual data entry.
- Demonstrate practical use of NLP in Information Extraction.
- Provide a clean and interactive web interface.

---

# ✨ Features

- ✅ Upload PDF documents
- ✅ Upload DOCX documents
- ✅ Upload TXT files
- ✅ Extract Name
- ✅ Extract Email Address
- ✅ Extract Phone Number
- ✅ Extract Location
- ✅ Extract Website / Social Links
- ✅ Handles resumes and general text documents
- ✅ Responsive and modern UI
- ✅ Cloud deployable

---

# 🧠 NLP Techniques Used

The project combines multiple Natural Language Processing techniques.

### 1. Named Entity Recognition (NER)

Used for identifying entities like:

- Person Names
- Locations

Library Used:

- spaCy

---

### 2. Regular Expressions (Regex)

Used for extracting structured patterns such as:

- Email IDs
- Phone Numbers
- URLs

Regex provides fast and highly accurate pattern matching.

---

### 3. Rule-Based Extraction

Some documents (especially resumes) have inconsistent formatting.

Additional rule-based filtering is used to:

- Improve name detection
- Remove unwanted entities
- Clean extracted data
- Reduce false positives

---

# 🛠 Tech Stack

## Programming Language

- Python 3

## Backend

- Flask

## NLP Library

- spaCy
- en_core_web_sm Language Model

## Pattern Matching

- Python Regular Expressions (re)

## Document Processing

- PDFPlumber (PDF Reader)
- python-docx (DOCX Reader)

## Frontend

- HTML5
- CSS3
- Jinja2 Templates

## Deployment

- Gunicorn
- Render Cloud Platform

---

# 📂 Supported Input Formats

| Format | Supported |
|---------|-----------|
| PDF | ✅ |
| DOCX | ✅ |
| TXT | ✅ |

Examples include:

- Resume
- CV
- Introduction Paragraph
- Email Content
- Chat Conversations
- Personal Profile
- Bio
- Notes

---

# 📤 Output

The application extracts and displays:

- Name
- Email Address
- Phone Number
- Location
- Links

Example:

```
Name:
Durvesh Nayak

Email:
durveshnayak6@gmail.com

Phone:
+91 9021282474

Location:
Sangli, Maharashtra, India

Links:
https://linkedin.com/in/...
https://github.com/...
```

---

# 📁 Project Structure

```
Contact-Extractor/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/contact-extractor.git
```

Move inside project

```bash
cd contact-extractor
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

Run the Application

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 📚 Libraries Used

| Library | Purpose |
|----------|----------|
| Flask | Web Framework |
| spaCy | Named Entity Recognition |
| re | Pattern Matching |
| pdfplumber | PDF Text Extraction |
| python-docx | DOCX Reading |
| Jinja2 | HTML Template Rendering |
| Gunicorn | Production WSGI Server |

---

# 🧪 Test Cases

Successfully tested on:

- Student Resume
- Professional Resume
- Introduction Paragraph
- Chat Messages
- Email Content
- Personal Biography
- Plain Text Documents

---

# 🚀 Future Enhancements

- OCR Support for Image Documents
- Custom-trained NER Model
- Multiple Language Support
- Batch Document Processing
- Export Results to CSV/Excel
- REST API Integration
- Database Storage
- AI-powered Contact Classification

---

# 🎓 Academic Relevance

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Named Entity Recognition (NER)
- Information Extraction
- Text Mining
- Pattern Recognition
- Web Application Development
- Cloud Deployment

---

# 📖 Resources & References

### Official Documentation

- Python Documentation
- Flask Documentation
- spaCy Documentation
- PDFPlumber Documentation
- python-docx Documentation
- Render Documentation
- Gunicorn Documentation

### Concepts Used

- Natural Language Processing
- Named Entity Recognition
- Regular Expressions
- Information Extraction
- Text Processing
- Document Parsing

---

# 👨‍💻 Developed By

**Durvesh Rajesh Nayak**

Final Year B.Tech Computer Science & Engineering

---

# ⭐ If you found this project useful, consider giving it a Star!
