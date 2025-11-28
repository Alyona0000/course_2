#T20.27 Застосувати клас Decks для моделювання розкладів при грі у
#преферанс. У цю гру грають колодою з 32 карт, починаючи з 7, роздають 3
#гравцям по 10 карт, 2 карти залишаються у «прикупі». Старшинство карт – у
#порядку зростання гідності. На основі аналізу власних карт один з гравців
#може вибороти право визначати гру. Цей гравець бере прикуп, скидає 2
#«зайві» карти та оголошує козирну масть, яка «б’є» інші масті, а також
#кількість взяток, які він зобов’язується взяти. При кожному ході кожен з
#гравців кладе 1 карту та розігрується 1 взятка, яку забирає старша карта або
#козирна карта (старша з козирних карт, якщо їх декілька). Кожен з гравців
#зобов’язаний класти карту тієї масті, з якої зроблено хід. Якщо цієї масті
#немає, - то козирну карту. Якщо козирної карти немає, то будь-яку карту.
#Право наступного ходу отримує гравець, який взяв останню взятку.
#Для того, щоб при власному першому ході гарантовано взяти всі 10 взяток
#треба мати у масті, яка буде оголошена козирною, одну з таких комбінацій
#карт:

# туз, король, дама, валет;
# туз, король, дама та 2 будь-які менші карти;
# туз, король та 4 будь-які менші карти;
# туз та 6 будь-яких менших карт;
# всі вісім карт однієї масті.
#Треба також мати всі старші карти в усіх інших наявних мастях (або
#комбінацію у ще одній масті туза, короля, дами та 2 будь-яких менших карт
#за умови не більше 5 карт у козирній масті).
#Знайти ймовірність наявності на будь-якій руці розкладу, що дозволяє за
#умови власного першого ходу гарантовано взяти всі 10 взяток:
#а) без урахування прикупу;


#Розв’язати задачу методом Монте-Карло з використанням масивів numpy.
#Векторизувати програмний код, наскільки можливо.



import numpy as np, json

class Decks:
    def __init__(self, num_decks=1, min_rank=7):
        # Формує вказану кількість колод карт.
        # Аргументи:
        #   num_decks – кількість колод
        #   min_rank – мінімальний ранг карти (2..14), де 11=J, 12=Q, 13=K, 14=A

        if not (7 <= min_rank <= 14):
            raise ValueError("Мінімальний ранг має бути від 7 до 14")
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

        # Створюємо список незалежних колод (кожна перемішана)
    def card_to_string(self, card: int) -> str:
        suit_names = {1: "♠️", 2: "♥️", 3: "♦️", 4: "♣️"}
        rank_names = {7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{suit_names[card // 100]}  {rank_names[card % 100]}"

    def set_to_string(self, set: np.ndarray) -> str: # преобразует набор карт в строковое представление
        return "  ".join([self.card_to_string(card) for card in set])
    
    def deal(self, num_players, num_cards):
        # Роздає кожному гравцю по num_cards карт з КОЖНОЇ колоди
        num_decks = len(self.all_decks)
        # Знаходимо кількість колод

        dealt = [[] for _ in range(num_players)]
        # Створюємо список гравців; у кожного буде список карт із кожної колоди

        # Роздача з колоди окремо
        for deck_index, deck in enumerate(self.all_decks):
            #print(f"\nРоздаємо карти з колоди №{deck_index + 1}")
            

            if num_players * num_cards > len(deck): # перевірка чи вистачає карт в колоді
                raise ValueError(f"У колоді №{deck_index + 1} недостатньо карт!")

            for i in range(num_players):
                player_cards = deck[:num_cards]
                # Беремо перші num_cards карт із поточної колоди

                deck = deck[num_cards:] # в кінці повинно залишитись 2 карти 
                # Зменшуємо колоду після роздачі

                dealt[i].append(player_cards)
                # Додаємо карти з цієї колоди поточному гравцю
                s = self.set_to_string(player_cards)
               # print(f"  Гравець {i + 1} отримав з колоди {s}")

            # Оновлюємо стан колоди після роздачі
            self.all_decks[deck_index] = deck

        #print("\nПісля роздачі залишок карт у кожній колоді:")
        #for i, deck in enumerate(self.all_decks, start=1):
          #  print(f"  Колода {i}: {len(deck)} карт залишилось") # повинно бути по 2 карти в кожній колоді

        return dealt
        # Повертаємо список: у кожного гравця — масив карт із кожної колоди





def get_cards_by_suit(hand_numbers, suit_index):
    return hand_numbers[ hand_numbers // 100 == suit_index]

def check_winning_combination(hand_numbers,suit_index):
    #розрахувати сумарний ранг та кількість карт у розрізі масті
    dd = get_cards_by_suit(hand_numbers,suit_index)
    dd = np.sort(dd)[::-1]
    #print(dd)
    numbers_of_cards = np.size(dd)
    #print(ff_size)
    rang = np.sum(dd%100)
    #print(rang)
    # мінімальний ранг для виграшу 39 для 3 карт туз король дама
    # індекс в масиві це кількість карт
    min_rangs = np.array([ 0, 14, 27, 39, 50, 54, 61, 71, 84])
    min_rang_for_hand = min_rangs[numbers_of_cards]
    number_of_top_cards = numbers_of_cards if numbers_of_cards <=4 else 8 - numbers_of_cards # визначаємо скільки верхніх карт потрібно для перевірки
    rang_top_cards = np.sum(dd[:number_of_top_cards] %100) 
    min_rang_for_top_cards = min_rangs[number_of_top_cards]
   # print(min_rang_for_top_cards,rang_top_cards,number_of_top_cards,numbers_of_cards)
    #print(min_rang_for_hand)
    return rang >= min_rang_for_hand and  rang_top_cards >= min_rang_for_top_cards



def case_5(hand_numbers):
    if not np.any(np.bincount(hand_numbers//100)>=4):
        return False
    
    r = np.array([
        check_winning_combination(hand_numbers,1),
        check_winning_combination(hand_numbers,2),
        check_winning_combination(hand_numbers,3),
        check_winning_combination(hand_numbers,4)
    ])
    #print(r)
    return np.all(r)

# Приклад використання:
num_decks= 50000
num_players = 3
d = Decks(num_decks, min_rank=7)  #1 колоди, карти від 7 до туза
#print("Кількість колод:", len(d.all_decks))  # значення кількості колод



hands = d.deal(num_players, num_cards=10)  # Роздаємо по 5 карт кожному гравцю з кожної колоди

#print(json.dumps(hands, indent= 4))

ll=np.array(hands)
hands = ll.reshape(num_players*num_decks,10)


case_5_result =np.array([case_5(player_cards) for player_cards in hands ])
print(case_5_result)


f = case_5_result[case_5_result]
print("кількість розкладів", case_5_result.size)
print(f"кількість виграшних розкладів:  {f.size}")
print(f"вирогідність сценарію: {(f.size/case_5_result.size):.8f}")

print("=============================")
wins = hands[case_5_result]
print(wins)
for w in wins:
    f = np.sort(np.array(w))[::-1]
    s = d.set_to_string(f)
    print(s)