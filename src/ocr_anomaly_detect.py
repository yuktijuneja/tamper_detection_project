import difflib
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

def compare_pdfs(original_path, tampered_path):
    original_text = extract_text_from_pdf(original_path)
    tampered_text = extract_text_from_pdf(tampered_path)
    
    print(f"Differences between {original_path} and {tampered_path}:\n")
    diff = difflib.ndiff(original_text.split(), tampered_text.split())
    for d in diff:
        if d.startswith('- ') or d.startswith('+ '):
            print(d)

if __name__ == "__main__":
    compare_pdfs("samples/degree_original.pdf", "samples/degree_tampered.pdf")
