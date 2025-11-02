import numpy as np


def roll_two_dice(n=1):
    """Функція для кидання двох кубиків n разів"""
    cube1 = np.random.randint(1, 7, size=n)
    cube2 = np.random.randint(1, 7, size=n)
    s = cube1 + cube2   

    # Якщо лише один кидок — теж повертай масив
    if n == 1:
        print(f"Випало: {cube1[0]} і {cube2[0]} => сума: {s[0]}")
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


def simulate_2(n):
    """Симуляція гри 'Крап' для n гравців"""
    print(f"\nСимуляція {n} гравців у 'Крап' розпочинається!")
    print("---------------------------------------------")

    # Перший кидок усіх гравців
    first_throw = roll_two_dice(n)

    # Хто одразу виграв або програв
    win_mask = (first_throw == 7) | (first_throw == 11)
    lose_mask = (first_throw == 2) | (first_throw == 3) | (first_throw == 12)

    # Ті, хто продовжує гру
    ongoing_mask = ~(win_mask | lose_mask)
    points = first_throw[ongoing_mask]

    wins = np.sum(win_mask)
    losses = np.sum(lose_mask)

    print(f"Після першого кидка: виграли = {wins}, програли = {losses}, залишилось у грі = {np.sum(ongoing_mask)}")

    # Гра триває, поки хтось ще в грі
    while len(points) > 0:
        new_throws = roll_two_dice(len(points))
        still_playing = []

        for i, throw in enumerate(new_throws):
            if throw == points[i]:
                wins += 1
            elif throw == 7:
                losses += 1
            else:
                still_playing.append(points[i])  # залишається у грі

        points = np.array(still_playing)
        print(f"Раунд завершено: виграли = {wins}, програли = {losses}, залишилось у грі = {len(points)}")

    # --- фінальний підрахунок результатів ---
    win_rate = wins / n
    print("---------------------------------------------")
    print(f"Кількість гравців: {n}")
    print(f"Кількість виграшів: {wins}")
    print(f"Кількість програшів: {losses}")
    print(f"Ймовірність виграшу: {round(win_rate, 4)}")

    return win_rate


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

        simulate_2(n)
    else:
        print("Помилка: потрібно вибрати 1 або 2.")


if __name__ == "__main__":
    main()
