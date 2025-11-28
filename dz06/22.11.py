import os

def compare_dirs(dir1, dir2, output_file):
    """
    Порівнює файли з однаковими іменами у двох каталогах.
    Якщо розміри відрізняються — записує різницю у текстовий файл.
    """

    # Отримуємо списки файлів
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))

    # Спільні файли за іменами
    common_files = files1 & files2

    with open(output_file, "w", encoding="utf-8") as out:
        for fname in sorted(common_files):
            path1 = os.path.join(dir1, fname)
            path2 = os.path.join(dir2, fname)

            # Перевіряємо, що елементи — саме файли
            if os.path.isfile(path1) and os.path.isfile(path2):
                size1 = os.path.getsize(path1)
                size2 = os.path.getsize(path2)

                if size1 != size2:
                    diff = size2 - size1
                    out.write(
                        f"{fname}: {size1} байт  →  {size2} байт  (різниця: {diff} байт)\n"
                    )

    print("Готово! Результат записано у:", output_file)


# ---------------------------------------------------------
# ПРИКЛАД ЗАПУСКУ ПРОГРАМИ (ти міняєш шляхи на свої)
# ---------------------------------------------------------
if __name__ == "__main__":

    # Каталоги для порівняння
    dir_a = r"C:\Users\alenk\Documents\Homework\folder1"
    dir_b = r"C:\Users\alenk\Documents\Homework\folder2"



    # Файл для вихідних даних
    out_file = "result.txt"

    compare_dirs(dir_a, dir_b, out_file)
