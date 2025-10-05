# Т17.4
# Декоратор для перевірки, чи всі аргументи є рядками
def strings_only(func):
    def wrapper(*args, **kwargs):
        # Перевірка всіх позиційних аргументів
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("Всі позиційні аргументи мають бути рядками")
        # Перевірка всіх іменованих аргументів
        for value in kwargs.values():
            if not isinstance(value, str):
                raise TypeError("Всі іменовані аргументи мають бути рядками")
        # Якщо всі аргументи рядки — викликаємо оригінальну функцію
        return func(*args, **kwargs)
    return wrapper


# Функція, яка повертає список унікальних рядків у порядку введення
@strings_only  # застосовуємо декоратор strings_only
def unique_strings(*lines):
    seen = set()      # множина для відстеження вже зустрінутих рядків
    result = []       # список результату
    for line in lines:
        if line not in seen:  # якщо рядка ще не було
            seen.add(line)    # додаємо його в множину
            result.append(line)  # і в результат
    return result


# Перевірка роботи
if __name__ == "__main__":
    print(unique_strings("apple", "banana", "apple", "orange"))
    # ['apple', 'banana', 'orange']  — унікальні рядки у тому порядку, як вони подані

    # Викличе помилку, бо 123 не є рядком
    # print(unique_strings("apple", 123, "banana"))



# Т17.9 
# Декоратор для кешування результатів виклику функції з одним аргументом n
def cache_results(max_n):
    def decorator(func):
        cache = [None] * (max_n + 1)  # список для кешу (індекси 0..max_n)
        def wrapper(n):
            nonlocal cache  # вказуємо, що будемо змінювати список cache
            if not (1 <= n <= max_n):  # перевірка, чи n у допустимому діапазоні
                raise ValueError(f"n має бути в межах 1..{max_n}")
            if cache[n] is not None:   # якщо результат уже є у кеші
                return cache[n]
            result = func(n)           # обчислюємо результат
            cache[n] = result          # зберігаємо його в кеш
            return result
        return wrapper
    return decorator


@cache_results(100)  # кешуємо результати для n від 1 до 100
def fibonacci(n):
    # Базові випадки
    if n == 1 or n == 2:
        return 1
    # Рекурсивний випадок
    return fibonacci(n - 1) + fibonacci(n - 2)


# Перевірка роботи
if __name__ == "__main__":
    print(fibonacci(10))   # 55
    print(fibonacci(20))   # 6765
    # print(fibonacci(101))  # ValueError (бо виходить за межі кешу)



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
