# src/ingest/parser.py
from typing import Tuple
import os
import logging

logger = logging.getLogger(__name__)

def parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def parse_docx(file_path: str) -> str:
    from docx import Document
    doc = Document(file_path)
    parts = [p.text for p in doc.paragraphs]
    return "\n".join(parts)

def parse_pdf(file_path: str) -> str:
    import pdfplumber
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text() or "")
    return "\n".join(texts)

def parse_file(file_path: str) -> Tuple[str, dict]:
    ext = os.path.splitext(file_path)[1].lower()
    meta = {"source": os.path.basename(file_path)}
    try:
        if ext == ".pdf":
            text = parse_pdf(file_path)
        elif ext in [".docx", ".doc"]:
            text = parse_docx(file_path)
        elif ext in [".txt", ".md"]:
            text = parse_txt(file_path)
        else:
            text = parse_txt(file_path)
        return text, meta
    except Exception as e:
        logger.exception("Failed to parse %s: %s", file_path, e)
        return "", meta
