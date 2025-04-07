import fitz
import tkinter as tk
from tkinter import filedialog


def select_and_reverse_pdf():
    root = tk.Tk()
    root.withdraw()  # GUI 창 숨기기

    input_pdf = filedialog.askopenfilename(title="PDF 파일 선택", filetypes=[("PDF Files", "*.pdf")])
    if not input_pdf:
        print("❌ 파일이 선택되지 않았습니다.")
        return

    output_pdf = input_pdf.replace(".pdf", "_reversed.pdf")

    doc = fitz.open(input_pdf)
    new_doc = fitz.open()

    for i in reversed(range(len(doc))):
        new_doc.insert_pdf(doc, from_page=i, to_page=i)

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()
    print(f"✅ 변환 완료: {output_pdf}")


select_and_reverse_pdf()
