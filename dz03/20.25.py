# написати код що формує колоди карт в конструкторі вказати кількість колод арг мин карт(ранг)
# гравцям роздавати карти з кожної колоди, тобто у гравців буде масив карт з кожної колоди

import numpy as np

class Decks:
    def __init__(self, num_decks=3, min_rank=2):
        # Формує вказану кількість колод карт.
        # Аргументи:
        #   num_decks – кількість колод
        #   min_rank – мінімальний ранг карти (2..14), де 11=J, 12=Q, 13=K, 14=A

        if not (2 <= min_rank <= 14):
            raise ValueError("Мінімальний ранг має бути від 2 до 14")
        # Перевірка правильності мінімального рангу

        suits = np.array([100, 200, 300, 400])
        # Кожній масті відповідає свій код:
        # 100 – піки ♠, 200 – черви ♥, 300 – бубни ♦, 400 – хрести ♣

        ranks = np.arange(min_rank, 15)
        # Формуємо ранги карт від min_rank до 14 (14 – це туз)

        one_deck = np.array([ranks + s for s in suits])
        # Створюємо одну колоду: до кожного коду масті додаємо ранг
        # Наприклад, 100+7=107 → сімка піка

        one_deck = one_deck.flatten()
        # Перетворюємо двовимірний масив у плоский (усі карти в один ряд)

        # Створюємо список незалежних колод (кожна перемішана)
        self.all_decks = [np.random.permutation(one_deck) for _ in range(num_decks)]
        # Кожна колода існує окремо й має свій порядок карт
    def card_to_string(self, card: int) -> str:
        suit_names = {1: "♠️", 2: "♥️", 3: "♦️", 4: "♣️"}
        rank_names = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{suit_names[card // 100]}  {rank_names[card % 100]}"

    def set_to_string(self, set: np.ndarray) -> str:
        return "  ".join([self.card_to_string(card) for card in set])
    
    def deal(self, num_players, num_cards):
        # Роздає кожному гравцю по num_cards карт з КОЖНОЇ колоди
        num_decks = len(self.all_decks)
        # Знаходимо кількість колод

        dealt = [[] for _ in range(num_players)]
        # Створюємо список гравців; у кожного буде список карт із кожної колоди

        # Роздача з кожної колоди окремо
        for deck_index, deck in enumerate(self.all_decks):
           # print(f"\nРоздаємо карти з колоди №{deck_index + 1}")
            # Виводимо номер поточної колоди

            if num_players * num_cards > len(deck):
                raise ValueError(f"У колоді №{deck_index + 1} недостатньо карт!")

            for i in range(num_players):
                player_cards = deck[:num_cards]
                # Беремо перші num_cards карт із поточної колоди

                deck = deck[num_cards:]
                # Зменшуємо колоду після роздачі

                dealt[i].append(player_cards)
                # Додаємо карти з цієї колоди поточному гравцю

                #print(f"  Гравець {i + 1} отримав з колоди {deck_index + 1}: {player_cards}")

            # Оновлюємо стан колоди після роздачі
            self.all_decks[deck_index] = deck

       # print("\nПісля роздачі залишок карт у кожній колоді:")
        #for i, deck in enumerate(self.all_decks, start=1):
            #print(f"  Колода {i}: {len(deck)} карт залишилось")

        return dealt
        # Повертаємо список: у кожного гравця — масив карт із кожної колоди

# Метод Монте-Карло — это численный метод, использующий случайные числа для решения сложных задач в различных областях,
# таких как физика, экономика и управление проектами.

def case_1 (hand_numbers):    
    suit = hand_numbers // 100     # масть карти
    # Перевірка на "каре" (4 карти одного рангу)
    uniq_values, counts = np.unique(suit, return_counts=True)
    return np.any(counts == 4)


def case_2(hand_numbers):
    suit = hand_numbers // 100      # визначає масть карти 
    ranks = hand_numbers % 100      # гідність карт (2–14)
    
    # визначаємо 5 карт однієї масті
    #опрреділяєт унікальні значення та рахує їхню кількість 
    uniq_values, counts = np.unique(suit, return_counts=True)
    cond_1 = uniq_values.size == 1 and counts[0] == 5
    sort = np.sort(hand_numbers)
    d = [1, 2, 3, 4, 5]
    c = sort - d
    uniq_values, counts =np.unique(c, return_counts=True)
    cond_2 = uniq_values.size == 1 
    
   # результат = тру якщо 4 масті рівні, яещо 5 мастей рівні + гдність зростає на 1 
   # 5 карт мають однакову масть,
    return cond_1 and cond_2



# Приклад використання:
d = Decks(num_decks=5000, min_rank=7)  # 3 колоди, карти від 7 до туза
print("Кількість колод:", len(d.all_decks))  # Виводимо кількість колод

hands = d.deal(num_players=4, num_cards=5)  # Роздаємо по 5 карт кожному гравцю з кожної колоди

print("\nКарти гравців:")

case_1_resold = []
case_2_resold = []


for i, player in enumerate(hands, start=1):
    print(f"Гравець {i}:")
    for deck_index, cards_from_deck in enumerate(player, start=1):
        c_1= case_1(cards_from_deck)
        c_2= case_2(cards_from_deck)
       # print(f"  З колоди {deck_index}: {d.set_to_string(cards_from_deck)},  {c_1}")
        case_1_resold.append(c_1)
        case_2_resold.append(c_2)

case_1_resold= np.array(case_1_resold)
case_2_resold= np.array(case_2_resold)
print("всього", case_1_resold.size)
d = case_1_resold[case_1_resold]
f = case_2_resold[case_2_resold]
print("кількість випадків коли 4 карти", d.size)
print("кількість випадків коли 5 однакових карт", f.size)
print("вирогідність 1-шого сценарію", d.size/case_1_resold.size)
print("вирогідність 2-шого сценарію", f.size/case_2_resold.size)