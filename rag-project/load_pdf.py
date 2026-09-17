from pypdf import PdfReader

pdf_path = "Unit-II DSA.pdf"

reader = PdfReader(pdf_path)

all_text = ""

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    all_text += f"\n--- Page {page_number} ---\n"
    all_text += text

with open("dsa_text.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("PDF text extracted successfully!")
print("Total pages:", len(reader.pages))
print("Saved as: dsa_text.txt")