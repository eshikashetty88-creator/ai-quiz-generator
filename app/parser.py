from pyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    
    return text

with open("sample.pdf", "rb") as file:
    text = extract_text_from_pdf(file)
    print(text)