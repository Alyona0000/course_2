import numpy as np


def roll_two_dice(n=1):
    """Функція для кидання двох кубиків n разів"""
    cube1 = np.random.randint(1, 7, size=n)
    cube2 = np.random.randint(1, 7, size=n)
    s = cube1 + cube2

    if n == 1:
        print(f"Випало: {cube1[0]} і {cube2[0]} => сума: {s[0]}")
        return s[0]
    else:
        return s


def play_craps():
    """Одна гра 'Крап' (з інтерактивом)"""
    print("Гра 'Крап' починається!")
    print("--------------------------")

    first_throw = roll_two_dice()

    if first_throw in (7, 11):
        print("Ви виграли! (7 або 11)")
        return True
    elif first_throw in (2, 3, 12):
        print("Ви програли! (2, 3 або 12)")
        return False

    point = first_throw
    print(f"Ваше число (point): {point}")
    print("Щоб зробити кидок, введіть 0.\n")

    while True:
        move = input("Ваш хід (0 - кинути кубики): ")
        if move != "0":
            print("Помилка: введіть 0!")
            continue

        throw = roll_two_dice()

        if throw == point:
            print("Ви виграли! (випало ваше число)")
            return True
        elif throw == 7:
            print("Ви програли! (випала 7)")
            return False


def simulate(n):
    """Симуляція n ігор (без інтерфейсу)"""
    # Перші кидки для всіх ігор
    first_throw = roll_two_dice(n)

    # Миттєві виграші та поразки
    wins = (first_throw == 7) | (first_throw == 11)
    losses = (first_throw == 2) | (first_throw == 3) | (first_throw == 12)

    # Ігри, що продовжуються
    ongoing = ~(wins | losses)
    points = first_throw[ongoing]

    # Моделюємо подальші кидки для тих, у кого є point
    for i, point in enumerate(points):
        while True:
            throw = np.random.randint(2, 13)
            if throw == point:
                wins[ongoing.nonzero()[0][i]] = True
                break
            elif throw == 7:
                losses[ongoing.nonzero()[0][i]] = True
                break

    # Підрахунок результатів
    total_wins = np.sum(wins)
    win_rate = total_wins / n

    print("--------------------------")
    print(f"Кількість ігор: {n}")
    print(f"Кількість виграшів: {total_wins}")
    print(f"Ймовірність виграшу: {round(win_rate, 4)}")


def main():
    """Основна частина програми"""
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
            return

        n = int(n)
        if n <= 0:
            print("Помилка: кількість ігор має бути додатною!")
            return

        simulate(n)
    else:
        print("Помилка: потрібно вибрати 1 або 2.")


if __name__ == "__main__":
    main()





























