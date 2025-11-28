import os
import zipfile

# ============================================================
# 1. Створення ОГРОМНОГО файлу
# ============================================================
def create_big_single_file(path, size_mb):
    """Створює великий файл указаного розміру (МБ)."""
    size_bytes = size_mb * 1024 * 1024

    print(f"Створюємо файл {path} ({size_mb} МБ)...")
    with open(path, "wb") as f:
        f.write(os.urandom(size_bytes))
    print("Файл створено!\n")


# ============================================================
# 2. Створення ZIP-архіву
# ============================================================
def make_zip(source_dir, zip_name):
    """Створює ZIP-архів з каталогу."""
    print("Створюємо ZIP-архів...")

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_dir)
                z.write(full_path, rel_path)

    print(f"Архів створено: {zip_name}")
    return zip_name


# ============================================================
# 3. Розбиття архіву на частини
# ============================================================
def split_file(file_path, max_size):
    """
    Розбиває файл на частини max_size байт.
    Частини мають формат:
        file.zip.0001
        file.zip.0002
    """
    part_num = 1

    print("Починаємо розбиття архіву...")

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(max_size)
            if not chunk:
                break

            new_file = f"{file_path}.{part_num:04d}"
            with open(new_file, "wb") as part:
                part.write(chunk)

            print(f"Створено частину: {new_file}")
            part_num += 1

    print("\nРозбиття завершено!\n")


# ============================================================
# 4. Головна функція — все разом
# ============================================================
def full_process(folder, huge_file_size_mb, max_part_size_mb):
    """
    Створює великий файл → архівує → розбиває.
    """

    # 1) Створення великого файлу
    os.makedirs(folder, exist_ok=True)
    huge_file_path = os.path.join(folder, "HUGE_TEST.bin")
    create_big_single_file(huge_file_path, huge_file_size_mb)

    # 2) Створення архіву
    zip_name = os.path.basename(folder.rstrip("\\/")) + ".zip"
    zip_path = os.path.join(folder, zip_name)
    make_zip(folder, zip_path)

    # 3) Розбиття
    max_part_size_bytes = max_part_size_mb * 1024 * 1024
    split_file(zip_path, max_part_size_bytes)


# ============================================================
# 5. Запуск
# ============================================================
if __name__ == "__main__":

    base = r"C:\Users\alenk\Repository\Course_2\dz06\folder1"

    full_process(
        folder=base,
        huge_file_size_mb=200,       # РОЗМІР великого файлу
        max_part_size_mb=10          # РОЗМІР кожної частини архіву
    )
