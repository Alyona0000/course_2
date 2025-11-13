#написати код що формує колоди карт в конструкторі вказати кількість колод арг мин карт(рагн)
# гравцям розавати карти з кожної колоди, тобто у гравцях буде масив карт з кожної колоди
import numpy as np

class Decks:
    def __init__(self, num_decks=1, min_rank=2):
        # Формує вказану кількість колод карт.
        # Аргументи:
        #   num_decks – кількість колод
        #   min_rank – мінімальний ранг карти (2..14), де 11=J, 12=Q, 13=K, 14=A

        if not (2 <= min_rank <= 14):
            raise ValueError("Мінімальний ранг має бути від 2 до 14")
        # Перевірка, щоб мінімальний ранг був у межах від 2 до 14

        suits = np.array([100, 200, 300, 400])
        # Кожній масті відповідає свій код:
        # 100 – піки ♠, 200 – черви ♥, 300 – бубни ♦, 400 – хрести ♣

        ranks = np.arange(min_rank, 15)
        # Формуємо ранги карт від min_rank до 14 (14 – це туз)

        one_deck = np.array([ranks + s for s in suits])
        # Створюємо одну колоду: до кожного коду масті додаємо ранг
        # Наприклад, 100+6=106 → шістка піка

        one_deck = one_deck.flatten()
        # Перетворюємо двовимірний масив у плоский (усі карти в один ряд)

        self.cards = np.tile(one_deck, num_decks)
        # Повторюємо одну колоду потрібну кількість разів

        self.cards = np.random.permutation(self.cards)
        # Перемішуємо всі карти випадковим чином

    def deal(self, num_players, num_cards):
        # Роздає кожному гравцю по num_cards карт
        if num_players * num_cards > len(self.cards):
            raise ValueError("У колоді недостатньо карт!")
        # Перевірка: чи вистачає карт на всіх

        dealt = []  # список для збереження карт кожного гравця

        for i in range(num_players):
            player_cards = self.cards[:num_cards]
            # Беремо перші num_cards карт для гравця

            self.cards = self.cards[num_cards:]
            # Зменшуємо колоду після роздачі

            dealt.append(player_cards)
            # Додаємо карти поточного гравця в список

            #displaying_cards = 
            print(f"Гравець {i+1} отримав:", player_cards)
            # Виводимо карти, отримані гравцем

        print("Залишок у колоді:", self.cards)
        # Показуємо, які карти залишились після роздачі

        return dealt
        # Повертаємо список розданих карт


# Приклад використання:
d = Decks(num_decks=1, min_rank=7)  # 3 колоди, карти від 6 до туза
print("Кількість карт у колоді:", len(d.cards))  # Виводимо кількість карт
hand = d.deal(num_players=4, num_cards=5)  # Роздаємо по 5 карт 4 гравцям
#print(displaying_cards)
#print(d.deal)

print("\nКарти гравців:")
for i, player in enumerate(hand, start=1):
    print(f"Гравець {i}:")
    for deck_index, cards_from_deck in enumerate(player, start=1):
        print(f"  З колоди {deck_index}: {cards_from_deck}")



   