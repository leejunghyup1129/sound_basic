import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs_alternating(pdf1_path, pdf2_path, output_path):
    pdf1 = PdfReader(pdf1_path)
    pdf2 = PdfReader(pdf2_path)
    writer = PdfWriter()

    pages1 = len(pdf1.pages)
    pages2 = len(pdf2.pages)
    max_pages = max(pages1, pages2)

    for i in range(max_pages):
        if i < pages1:
            writer.add_page(pdf1.pages[i])
        if i < pages2:
            writer.add_page(pdf2.pages[i])

    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)


def select_files():
    file1_path = filedialog.askopenfilename(title="Select the first PDF file", filetypes=[("PDF Files", "*.pdf")])
    if not file1_path:
        print("First PDF file not selected.")
        return

    file2_path = filedialog.askopenfilename(title="Select the second PDF file", filetypes=[("PDF Files", "*.pdf")])
    if not file2_path:
        print("Second PDF file not selected.")
        return

    output_path = file2_path.rsplit('/', 1)[0] + "/alternate.pdf"
    merge_pdfs_alternating(file1_path, file2_path, output_path)
    print(f"Merged PDF saved as: {output_path}")


# GUI 설정
root = tk.Tk()
root.withdraw()  # GUI 창 숨기기
select_files()
