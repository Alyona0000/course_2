import os
import hashlib
from datetime import datetime


def ensure_dir(path):
    """Створює каталог, якщо його не існує."""
    if not os.path.exists(path):
        os.makedirs(path)


def get_all_files(directory):
    """Рекурсивно отримує всі файли каталогу з относним шляхом."""
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, directory)
            file_dict[rel_path] = full_path
    return file_dict


def compare_dirs(dir1, dir2, output_file):
    """Основна функція порівняння каталогів."""

    ensure_dir(dir1)
    ensure_dir(dir2)

    files1 = get_all_files(dir1)
    files2 = get_all_files(dir2)

    common = sorted(set(files1.keys()) & set(files2.keys()))

    changes = []

    for rel in common:
        f1 = files1[rel]
        f2 = files2[rel]

        size1 = os.path.getsize(f1)
        size2 = os.path.getsize(f2)

        if size1 != size2:
            changes.append((rel, f1, f2, size1, size2))

    # ---------- ПИШЕМО ВИХІДНИЙ ФАЙЛ ----------
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("=" * 60 + "\n")
        out.write("              РЕЗУЛЬТАТ ПОРІВНЯННЯ ФАЙЛІВ\n")
        out.write("=" * 60 + "\n\n")

        out.write(f"Дата та час запуску: {datetime.now()}\n\n")
        out.write("Порівнювались каталоги:\n")
        out.write(f"  1) {dir1}\n")
        out.write(f"  2) {dir2}\n\n")

        out.write(f"Знайдено спільних файлів: {len(common)}\n")
        out.write(f"Файлів з різним розміром: {len(changes)}\n\n")

        if not changes:
            out.write("Всі спільні файли мають однаковий розмір.\n")
        else:
            out.write("--- ФАЙЛИ, ДЕ Є ВІДМІННОСТІ ---\n\n")
            for rel, f1, f2, s1, s2 in changes:
                diff = s2 - s1
                sign = "+" if diff > 0 else ""

                out.write(f"Файл: {rel}\n")
                out.write(f" → {f1} : {s1} байт\n")
                out.write(f" → {f2} : {s2} байт\n")
                out.write(f"   Різниця: {sign}{diff} байт\n\n")

        out.write("=" * 60 + "\n")
        out.write("                     КІНЕЦЬ ЗВІТУ\n")
        out.write("=" * 60 + "\n")

    print("Готово! Звіт записано у:", output_file)


# ==========================================================
# ПРИКЛАД ЗАПУСКУ
# ==========================================================
if __name__ == "__main__":
    base = r"C:\Users\alenk\Repository\Course_2\dz06"

    dir_a = os.path.join(base, "folder1")
    dir_b = os.path.join(base, "folder2")
    out_file = os.path.join(base, "result.txt")

    compare_dirs(dir_a, dir_b, out_file)
