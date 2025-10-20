import pdfplumber

with pdfplumber.open("data/lauinger (1).pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
print(text[:500])
