# Т17.16
# Декоратор для нумерації викликів функції
def print_with_call_number(func):
    call_count = 0  # лічильник викликів
    def wrapper(*args, **kwargs):
        nonlocal call_count   # використовуємо змінну з замикання
        call_count += 1       # збільшуємо лічильник
        # Друкуємо номер виклику з вирівнюванням у 3 позиції
        print(f"{call_count:3}: ", end="")
        # Викликаємо оригінальну функцію
        return func(*args, **kwargs)
    return wrapper


@print_with_call_number  # застосовуємо декоратор
def print_line(line):
    # Виводимо рядок, збережений у файлі
    # end="" щоб не дублювати символи нового рядка (\n), які вже є в line
    print(line, end="")


# Перевірка роботи для текстового файлу
if __name__ == "__main__":
    filename = "test.txt"  # назва файлу (замініть на свій)
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:       # читаємо файл построчно
                print_line(line) # кожен рядок друкується з номером
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
