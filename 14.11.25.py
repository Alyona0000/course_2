import os

def top_biggest_files(dirpath, top_n=10):
    if not os.path.exists(dirpath):
        print("❌ Папка не існує!")
        return []

    print(f"🔍 Обхід папки: {dirpath}")

    files_sizes = []

    for dir, listdir, listfiles in os.walk(dirpath):
        print(f"📁 Перевірка: {dir}")  # показує які папки обходить

        for file in listfiles:
            try:
                full_path = os.path.join(dir, file)
                size = os.path.getsize(full_path)
                files_sizes.append((full_path, size))
            except Exception as e:
                print("Помилка для файла:", file, "→", e)

    if not files_sizes:
        print("❗ У цій папці немає жодного файла!")
        return []

    # сортуємо
    files_sizes.sort(key=lambda x: x[1], reverse=True)

    result = [(path, size / (1024 * 1024)) for path, size in files_sizes[:top_n]]

    return result


# --- Виклик ---
path = r'D:\Навчання,робота\Програмування\Phyton  from O.V\22'

files = top_biggest_files(path, top_n=10)

print("\n=== РЕЗУЛЬТАТ ===")
for path, size_mb in files:
    print(f"{round(size_mb, 2)} MB — {path}")
