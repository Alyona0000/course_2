# T23.4 У документі Word містяться дати у форматі dd.mm.yyyy або
# підкреслення для запису дат вручну __.__.____ Знайти всі дати у тексті.
# Замість підкреслень вставити поточну дату. Зберегти оновлений документ.


import re
from datetime import datetime
from docx import Document

def process_dates(input_file, output_file):
    doc = Document(input_file)

    # регулярка для дат dd.mm.yyyy
    date_pattern = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")

    # регулярка для підкреслень __.__.____
    blank_pattern = re.compile(r"__\.__\.____")

    # поточна дата
    today = datetime.today().strftime("%d.%m.%Y")

    for paragraph in doc.paragraphs:
        text = paragraph.text

        # заміна підкреслень на сьогодні
        new_text = blank_pattern.sub(today, text)

        # (додатково: можна щось робити з датами, якщо треба, але тут не змінюємо)
        # знайти всі дати:
        found_dates = date_pattern.findall(new_text)
        # print(found_dates) — якщо потрібно подивитися

        paragraph.text = new_text

    doc.save(output_file)
    print("Готово! Файл оновлено:", output_file)


# ▶ Запуск
process_dates("input.docx", "output.docx")

