import os
import re
import fnmatch

def search_text_files(base_dir, mask, regex_pattern, output_file):
    """
    Пошук текстових файлів за маскою та регулярним виразом
    у каталозі та всіх підкаталогах.
    """

    regex = re.compile(regex_pattern)

    found_results = []

    for root, dirs, files in os.walk(base_dir):
        for filename in files:

            # Перевіряємо маску (*.txt, log_*.txt тощо)
            if fnmatch.fnmatch(filename, mask):

                full_path = os.path.join(root, filename)

                # Читаємо файл
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                except:
                    continue

                # Шукаємо збіги
                for i, line in enumerate(lines, start=1):
                    if regex.search(line):
                        found_results.append((full_path, i, line.strip()))

    # Записуємо результати
    with open(output_file, "w", encoding="utf-8") as out:

        out.write(f"Пошук у каталозі: {base_dir}\n")
        out.write(f"Маска файлів: {mask}\n")
        out.write(f"Регулярний вираз: {regex_pattern}\n\n")

        if not found_results:
            out.write("Збігів не знайдено.\n")
        else:
            out.write(f"Знайдено збігів: {len(found_results)}\n\n")
            for path, line_num, text in found_results:
                out.write(f"Файл: {path}\n")
                out.write(f"  Рядок {line_num}: {text}\n\n")

    print("Готово! Результат записано у:", output_file)


# ----------------------------------------------------------
# ПРИКЛАД ЗАПУСКУ (налаштовано під твої folder1)
# ----------------------------------------------------------
if __name__ == "__main__":

    base = r"C:\Users\alenk\Repository\Course_2\dz06"

    #  Саме той каталог, що ти хочеш
    base_dir = os.path.join(base, "folder1")

    mask = "*.txt"                     # шукати всі текстові файли
    regex_pattern = r".+"              # шукаємо будь-який непорожній текст
    output_file = os.path.join(base, "search_results.txt")

    search_text_files(base_dir, mask, regex_pattern, output_file)
