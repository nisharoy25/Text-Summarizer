# Handles file upload and extraction

from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(uploaded_file) -> str:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(uploaded_file) -> str:
    doc = docx.Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])
