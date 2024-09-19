import PyPDF2
import tabula


pdf_path = "/home/minh/Desktop/saoke/Thong tin ung ho qua STK VCB 0011001932418 ngay 11.09.2024.pdf"
def get_pdf_page_count(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return len(reader.pages)

def extract_text_from_pdf(pdf_file, page_num):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[page_num - 1]  # Pages are 0-indexed
        return page.extract_text()

def extract_table(pdf_path):
    return tabula.read_pdf(pdf_path, pages='1-5', multiple_tables=False)


tables = tabula.read_pdf(pdf_path, pages='1-5', multiple_tables=False)
print(tables[0].columns())

# # Extract tables from the PDF
# tables = tabula.read_pdf(pdf_path, pages='1', multiple_tables=True)
#
# print(tables)
