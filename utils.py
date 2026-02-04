import pdfplumber
from docx import Document

def read_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)

def split_clauses(text):
    lines = text.split("\n")
    clauses = [line.strip() for line in lines if len(line.strip()) > 40]
    return clauses
