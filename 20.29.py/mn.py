def card_title(card_code):
    if isinstance(card_code,str):
        if not card_code.lstrip("-").isdigit():
            print("Помилка: код має бути числом!")
            exit()
        d = int(card_code)
    elif isinstance(card_code,int):
        d = card_code
    else:
        print("ayayay")
        exit() 
# Перевіряємо, чи код є натуральним (додатним)
    if d <= 0:
        print("Помилка: код має бути натуральним числом (додатним)!")
        exit()

# Перевірка діапазону допустимих кодів
    if d < 102 or d > 414:
        return f"{d} - Код не коректний (має бути від 102 до 414)." 

    suit_code = d // 100  # перша цифра — масть
    rank_code = d % 100  # дві останні цифри — ранг
    suits = {
    1: "Піка ♠️",
    2: "Черви ♥️",
    3: "Бубни ♦️",
    4: "Хрести ♣️"
    }

    ranks = {
        11: "Валет (J)",
        12: "Дама (Q)",
        13: "Король (K)",
        14: "Туз (A)"
    } 
    # Перевірка, чи така карта існує
    if suit_code not in suits or not (2 <= rank_code <= 14):
        return f"{d} - Код не коректний: такої карти не існує."

    rank = ranks.get(rank_code, str(rank_code))
    suit = suits[suit_code]
    return f"Масть: {suit}, Ранг: {rank}"
    


card_code = input("Введіть код карти: ")
title = card_title(card_code)
print(title)
for suits_vel in range(1,5): 
    for rank_vel in range(2,15):  
        card_code = suits_vel * 100 + rank_vel
        title = card_title(card_code)
        print(title)


