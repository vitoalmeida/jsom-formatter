from PyPDF2 import PdfReader

pdf_path = 'brazil_law.pdf'
output_path = 'brazil_law_text.txt'

# Open the PDF file
with open(pdf_path, 'rb') as file:
    reader = PdfReader(file)
    extracted_text = ""

    # Start at page 12, go through each page until the end of the document
    for page_number in range(11, len(reader.pages)):  # Pages are zero-indexed
        page = reader.pages[page_number]
        extracted_text += page.extract_text() + "\n"

# Save the extracted text to a .txt file
with open(output_path, 'w', encoding='utf-8') as text_file:
    text_file.write(extracted_text)
