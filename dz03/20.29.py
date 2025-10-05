#T20.29 В умовах задачі T20.28 визначити ймовірність розкладів при
#фіксованому роздаванні. Зафіксувати на першій руці карти так, щоб
#найкраща потенційно козирна масть складалась з 4 карт а також 2 карти,
#скинуті після взяття прикупу. Виконати фіксоване роздавання. Знайти
#ймовірності того, що на другій та третій руці інші 4 карти цієї масті роздано
#у співвідношенні 4:0, 1:3, 2:2, 3:1, 0:4.

import numpy as np
from collections import Counter

def simulate_fixed_deal(n_sim=200_000, seed=42):
    np.random.seed(seed)

    suits = ['S', 'H', 'D', 'C']          # масті
    ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # 8 ранґів -> 32 карти
    deck = [f"{r}{s}" for s in suits for r in ranks]

    trump = 'S'  # фіксуємо козирну масть (можна ітеративно по всіх мастях)
    trump_cards = [c for c in deck if c.endswith(trump)]
    non_trump_cards = [c for c in deck if not c.endswith(trump)]

    # Фіксуємо, що на першій руці саме ці 4 козирі
    first_hand_trumps = trump_cards[:4]  # фіксовані 4 козирі на першій руці

    counts = Counter({'4:0':0, '3:1':0, '2:2':0, '1:3':0, '0:4':0})

    for _ in range(n_sim):
        # Випадково оберемо 6 некозирних карт для першої руки (щоб перша рука була 10 карт)
        first_hand_non_trumps = list(np.random.choice(non_trump_cards, size=6, replace=False))
        first_hand = set(first_hand_trumps + first_hand_non_trumps)

        # Формуємо колоду без карт першої руки
        remaining_deck = [c for c in deck if c not in first_hand]

        # Тепер потрібно зафіксувати 2 скинуті карти (після прикупу)
        # За логікою задачі ми фіксуємо, що скинуті карти НЕ є козирями,
        # щоб "інші 4 козирі" залишились у залишку для роздачі.
        remaining_non_trumps = [c for c in remaining_deck if not c.endswith(trump)]
        # Якщо по якимось причинам їх менше 2 (не має статися при коректній генерації), пропускаємо ітерацію
        if len(remaining_non_trumps) < 2:
            continue
        discarded = list(np.random.choice(remaining_non_trumps, size=2, replace=False))

        # Видаляємо скинуті з колоди для роздачі
        for d in discarded:
            remaining_deck.remove(d)

        # Тепер remaining_deck має 20 карт і серед них — саме 4 "інші" козирі
        # Перемішуємо і роздаємо по 10 карт двом гравцям
        np.random.shuffle(remaining_deck)
        second_hand = remaining_deck[:10]
        third_hand  = remaining_deck[10:20]

        second_trumps = sum(1 for c in second_hand if c.endswith(trump))
        third_trumps  = sum(1 for c in third_hand if c.endswith(trump))

        # Переконаємось, що сумарно в руках 2 та 3 саме 4 козирі (повинно бути так)
        total = second_trumps + third_trumps
        if total != 4:
            # Якщо трапилося інше (наприклад через помилку у вибірці), ігноруємо ітерацію
            continue

        key = f"{second_trumps}:{third_trumps}"
        if key in counts:
            counts[key] += 1

    # Перетворимо у ймовірності
    total_valid = sum(counts.values())
    probs = {k: (counts[k] / total_valid if total_valid > 0 else 0.0) for k in ['4:0','3:1','2:2','1:3','0:4']}
    return probs, counts, total_valid

if __name__ == "__main__":
    probs, counts, valid = simulate_fixed_deal(n_sim=200_000, seed=123)
    print(f"Кількість дійсних симуляцій: {valid}")
    print("Ймовірності розкладів (друга:третя):")
    for k in ['4:0','3:1','2:2','1:3','0:4']:
        print(f"{k}: {probs[k]:.4f}  ({counts[k]} випадків)")



