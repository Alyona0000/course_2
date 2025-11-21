#T21.4 У текстовому файлі містяться дати у форматі dd.mm.yyyy або
#підкреслення для запису дат вручну __.__.____ Знайти всі дати у тексті.
#Замість підкреслень вставити поточну дату. Зберегти оновлений текст.





import re

def vytyagty_daty(vkhid: str, vykhid: str) -> None:
    # читаємо текст
    with open(vkhid, "r", encoding="utf-8") as f:
        text = f.read()

    # шаблон дати dd.mm.yyyy
    pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"

    # знайти всі дати у тексті
    daty = re.findall(pattern, text)

    # записати знайдені дати у новий файл
    with open(vykhid, "w", encoding="utf-8") as f:
        for d in daty:
            f.write(d + "\n")

    print("Готово! Дати записані у файл:", vykhid)
    print("Знайдені дати:", daty)


# приклад виклику
vytyagty_daty(
    r"C:\Users\alenk\Repository\Course_2\dz05\text21_4.txt",
    r"C:\Users\alenk\Repository\Course_2\dz05\dates_only.txt"
)

