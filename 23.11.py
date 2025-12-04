# T23.11 У аркуші робочої книги MS Excel містяться дані про проекти та осіб,
# задіяних у цих проектах у формі:
# Project Person
import os
import openpyxl

# -------- функція: зчитати дані з Excel --------
def read_excel_data(filename, sheet_name='Sheet1'):
    # перевіряємо чи файл існує
    if not os.path.exists(filename):
        print("Файл не знайдено:", filename)
        return None

    # завантажуємо книгу
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet_name]

    data = []  # список з пар: (Project, Person)

    # проходимо по всіх рядках, пропускаємо заголовки
    for row in sheet.iter_rows(min_row=2, values_only=True):
        project, person = row
        data.append((str(project), str(person)))

    return data


# -------- функція: згрупувати дані --------
def group_by_project(data):
    result = {}

    for project, person in data:
        if project not in result:
            result[project] = []
        result[project].append(person)

    return result


# -------- функція: красиво вивести результат --------
def print_stats(projects):
    for project, people in projects.items():
        print(f"\nПроєкт: {project}")
        print("Учасники:", ", ".join(people))
        print("Кількість людей:", len(people))


# -------- main --------
if __name__ == "__main__":

    filename = "projects.xlsx"   # назва файла Excel
    sheet = "Sheet1"             # або інша назва листа

    data = read_excel_data(filename, sheet)
    if data:
        grouped = group_by_project(data)
        print_stats(grouped)




