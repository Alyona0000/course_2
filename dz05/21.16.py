#T21.16 В умовах завдання T21.15 Вам доручили також терміново надати
#список телефонів 100 найбільших боржників для їх подальшого
#інформування телефоном.
#Список повинен мати формат:
#<П.І.Б> <Телефон> <Борг>
#Використайте регулярні вирази для розв’язання задачі та складіть програму
#для формування списку.

import re

def top_100(vkhid, vykhid):
    # регулярки
    regex_pib = r"[А-ЯІЇЄҐA-Z][а-яіїєґa-z']+\s+[А-ЯІЇЄҐA-Z][а-яіїєґa-z']+\s+[А-ЯІЇЄҐA-Z][а-яіїєґa-z']+|" \
                r"[А-ЯІЇЄҐA-Z][а-яіїєґa-z']+\s+[А-ЯІЇЄҐA-Z]\.[А-ЯІЇЄҐA-Z]\."
    regex_phone = r"(телефон|тел\.?|ТЕЛЕФОН)[: ]*\+?\d[\d\- ]+"
    regex_debt = r"\b\d+\b$"

    records = []

    with open(vkhid, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            pib = re.search(regex_pib, line)
            phone = re.search(regex_phone, line, flags=re.IGNORECASE)
            debt = re.search(regex_debt, line)

            if pib and phone and debt:
                pib = pib.group()
                phone = phone.group()
                debt = int(debt.group())

                records.append((pib, phone, debt))

    # Сортуємо за боргом (спадання)
    records.sort(key=lambda x: x[2], reverse=True)

    # Беремо топ-10
    top = records[:10]

    # Записуємо у новий файл
    with open(vykhid, "w", encoding="utf-8") as f:
        for pib, phone, debt in top:
            f.write(f"{pib} {phone} {debt}\n")

    print("Готово! Записано 10 найбільших боржників у файл:", vykhid)
top_100(
    r"C:\Users\alenk\Repository\Course_2\dz05\borzhnyky.txt",
    r"C:\Users\alenk\Repository\Course_2\dz05\top10.txt"
)
