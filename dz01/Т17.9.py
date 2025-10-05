
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


