import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_file, start_page, end_page):
    # Проверка существования файла
    if not os.path.exists(input_file):
        print(f"Файл не найден: {input_file}")
        return

    reader = PdfReader(input_file)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    # Проверка диапазона
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        print("Некорректный диапазон страниц.")
        print(f"Всего страниц в документе: {total_pages}")
        return

    # PyPDF2 использует индексацию с 0
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])

    # Формирование имени выходного файла
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}-{start_page}-{end_page}{ext}"

    # Сохранение файла
    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"Готово! Новый файл: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <pdf_file> <start_page> <end_page>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    extract_pages(input_pdf, start, end)
