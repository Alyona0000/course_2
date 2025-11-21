#T21.6 У текстовому файлі міститься переписка декількох осіб електронною
#поштою. Скласти список контактів (адрес електронної пошти) осіб, що
#фігурують у даній переписці. Використати регулярні вирази.



import re

def znajty_emaily(vkhid: str, vykhid: str) -> None:
    # читаємо текст з файлу
    with open(vkhid, "r", encoding="utf-8") as f:
        text = f.read()

    # регулярний вираз для email-адрес
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # знаходимо всі email-и
    emails = re.findall(pattern, text)

    # видаляємо дублікати
    emails = sorted(set(emails))

    # записуємо у новий файл
    with open(vykhid, "w", encoding="utf-8") as f:
        for mail in emails:
            f.write(mail + "\n")

    print("Готово! Знайдено адрес:", len(emails))
    print("Список контактів записано у файл:", vykhid)


# Приклад виклику:
znajty_emaily(
    r"C:\Users\alenk\Repository\Course_2\dz05\emails.txt",
    r"C:\Users\alenk\Repository\Course_2\dz05\email_contacts.txt"
)
