import sys
from PyPDF2 import PdfReader, PdfWriter

def combine_pdfs(first_pdf_path, second_pdf_path, output_pdf_path="combined.pdf"):
    # Create PDF reader objects for both PDFs
    first_pdf_reader = PdfReader(first_pdf_path)
    second_pdf_reader = PdfReader(second_pdf_path)
    
    # Create a PDF writer object
    pdf_writer = PdfWriter()
    
    # Add all pages from the first PDF to the writer
    for page in first_pdf_reader.pages:
        pdf_writer.add_page(page)
    
    # Add all pages from the second PDF to the writer
    for page in second_pdf_reader.pages:
        pdf_writer.add_page(page)
    
    # Write the combined PDF to the output file
    with open(output_pdf_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)
    
    print(f"Combined PDF saved as '{output_pdf_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python combine_pdfs.py "first.pdf" "second.pdf"')
        sys.exit(1)
    
    first_pdf = sys.argv[1]
    second_pdf = sys.argv[2]
    
    combine_pdfs(first_pdf, second_pdf)
