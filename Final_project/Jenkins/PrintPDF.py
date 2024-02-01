import PyPDF2

# Open the PDF file
with open('CV.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(CV.pdf)

    # Get the total number of pages in the PDF
    num_pages = pdf_reader.numPages

    # Read each page and print its content
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        content = page.extractText()
        print(content)
