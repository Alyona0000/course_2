#написати код що формує колоду карт
import random

class Deck:
    def __init__(self, min_rank=2):
        self.suits = ["Піка ♠️", "Черви ♥️", "Бубни ♦️", "Хрести ♣️"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        if not (2 <= min_rank <= 10):
            raise ValueError("Мінімальна гідність має бути від 2 до 10")
        
        # Залишаємо тільки потрібні ранги
        self.ranks = self.ranks[self.ranks.index(str(min_rank)):]
        
        # Створюємо колоду
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append((rank, suit))
    
    def show(self):
        """Показати всі карти в колоді"""
        for card in self.cards:
            print(card)
        print(f"Всього карт: {len(self.cards)}")

    def shuffle(self):
        """Тасуємо колоду"""
        random.shuffle(self.cards)

    def deal(self, players, cards_per_player):
        """Роздаємо карти гравцям"""
        total_needed = players * cards_per_player
        if total_needed > len(self.cards):
            raise ValueError("Недостатньо карт у колоді")
        
        hands = []
        for i in range(players):
            hand = []
            for j in range(cards_per_player):
                hand.append(self.cards.pop())
            hands.append(hand)
        return hands


# ======= Обробка коду карти =======

a = input("Введіть код карти: ")

# Перевіряємо, чи це число (враховуючи можливий мінус)
if not a.lstrip("-").isdigit():
    print("Помилка: код має бути числом!")
    exit()

d = int(a)

# Перевіряємо, чи код є натуральним (додатним)
if d <= 0:
    print("Помилка: код має бути натуральним числом (додатним)!")
    exit()

# Перевірка діапазону допустимих кодів
if d < 102 or d > 414:
    print("Код не коректний (має бути від 102 до 414).")
    exit()

suit_code = d // 100      # перша цифра — масть
rank_code = d % 100       # дві останні цифри — гідність

# Словники мастей і гідностей
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
    print("Код не коректний: такої карти не існує.")
    exit()

# Формування результату
rank = ranks.get(rank_code, str(rank_code))
suit = suits[suit_code]

print(f"Масть: {suit}, Ранг: {rank}")

# ======= Приклад використання колоди =======

deck = Deck()
deck.shuffle()
hands = deck.deal(4, 5)

print("\nРоздані карти:")
for i, hand in enumerate(hands, 1):
    print(f"Гравець {i}: {hand}")
