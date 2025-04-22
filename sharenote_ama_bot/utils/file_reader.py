import os
import fitz  # PyMuPDF
import textract

def read_file(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        doc = fitz.open(file_path)
        return "".join([page.get_text() for page in doc])
    elif ext in [".doc", ".docx"]:
        text = textract.process(file_path)
        return text.decode("utf-8")
    else:
        raise ValueError("Unsupported file format.")
