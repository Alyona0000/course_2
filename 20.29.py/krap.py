import random

def roll_two_dice():
    # Функція для кидання двох кубиків
    cube1 = random.randint(1, 6)
    cube2 = random.randint(1, 6)
    s = cube1 + cube2
    print("Випало:", cube1, "і", cube2, "=> сума:", s)
    return s


def play_craps():
    print("Гра 'Крап' починається!")
    print("--------------------------")

    first_throw = roll_two_dice()
    print("Перший кидок:", first_throw)

    # Перевіряємо умови миттєвої перемоги або поразки
    if first_throw == 7 or first_throw == 11:
        print("Ви виграли одразу! (7 або 11)")
        return True

    if first_throw == 2 or first_throw == 3 or first_throw == 12:
        print("Ви програли одразу! (2, 3 або 12)")
        return False

    # Інакше встановлюємо "ваше число"
    point = first_throw
    print("Ваше число (point):", point)
    print("Кидайте далі, доки не випаде", point, "або 7.")
    print("Щоб зробити кидок, натисніть 0 і Enter.\n")

    # Цикл подальших кидків
    while True:
        move = input("Ваш хід (0 - кинути кубики): ")

        if move != "0":
            print("Помилка: введіть 0, щоб кинути кубики.")
            continue

        throw = roll_two_dice()

        if throw == point:
            print("Випало ваше число! Ви виграли!")
            return True

        if throw == 7:
            print("Випало 7. Ви програли.")
            return False

        print("Кидаємо далі...\n")


def simulate(n):
    # Функція для моделювання n ігор та підрахунку виграшів
    wins = 0
    i = 0

    while i < n:
        result = play_craps()
        if result == True:
            wins = wins + 1
        i = i + 1

    win_rate = wins / n
    print("--------------------------")
    print("Кількість ігор:", n)
    print("Кількість виграшів:", wins)
    print("Ймовірність виграшу:", round(win_rate, 4))


# --- Основна частина програми ---
print("Виберіть режим:")
print("1 - Зіграти один раз (з введенням 0)")
print("2 - Провести симуляцію кількох ігор")

choice = input("Ваш вибір: ")

if choice == "1":
    play_craps()

elif choice == "2":
    n = input("Скільки ігор провести?: ")

    if not n.isdigit():
        print("Помилка: введіть натуральне число!")
        exit()

    n = int(n)
    if n <= 0:
        print("Помилка: кількість ігор має бути додатною!")
        exit()

    simulate(n)

else:
    print("Помилка: потрібно вибрати 1 або 2.")
