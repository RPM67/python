import PyPDF2

def merge_pdfs(output_filename, *pdfs_with_ranges):
    merged_pdf = PyPDF2.PdfWriter()

    for pdf_file, page_range in pdfs_with_ranges:
        start_page, end_page = map(int, page_range.split('-'))

        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfReader(pdf)

            for page_num in range(start_page - 1, end_page):
                page = pdf_reader.pages[page_num]
                merged_pdf.add_page(page)

    with open(output_filename, 'wb') as output_file:
        merged_pdf.write(output_file)

if __name__ == "__main__":
    # Example usage:
    pdfs_to_merge = [
        ("12.pdf", "6-6"),
        ("13.pdf", "127-330"),
        # Add more PDFs with their respective page ranges as needed
    ]

    output_filename = "merged_document.pdf"
    merge_pdfs(output_filename, *pdfs_to_merge)

    print(f"Merged PDF saved to {output_filename}")
