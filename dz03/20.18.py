#T20.18 Вам пропонують зіграти у таку гру. Ви платите 1 одиницю грошей.
#Кидають 4 кості. Якщо сума не перевищить 9, Ви отримуєте 10 одиниць
#грошей. Чи будете Ви у виграші після багаторазового повторення гри?
#Розв’язати задачу методом Монте-Карло з використанням масивів numpy.
#Векторизувати програмний код.
#Гра вважається чесною, якщо сума винагороди дорівнює витраченим грошам,
#за умови ймовірного виграшу. Справедлива сума винагороди при вкладанні у
#кожну гру 1 одиниці грошей становить 1/p, де p – ймовірність виграшу.


import numpy as np

def monte_carlo_game(n_games=1_000_000, seed=42):
    np.random.seed(seed)
    # Кидаємо 4 кості n_games разів: числа від 1 до 6
    rolls = np.random.randint(1, 7, size=(n_games, 4))
    sums = np.sum(rolls, axis=1)
    wins = sums <= 9
    n_wins = np.sum(wins)
    p_win = n_wins / n_games
    # Виграш: 10 одиниць, програш: -1 одиниця (бо заплатили 1)
    profit = np.sum(wins * 10 - 1)
    avg_profit = profit / n_games
    fair_reward = 1 / p_win if p_win > 0 else float('inf')
    return {
        "n_games": n_games,
        "n_wins": n_wins,
        "p_win": p_win,
        "total_profit": profit,
        "avg_profit_per_game": avg_profit,
        "fair_reward": fair_reward
    }

if __name__ == "__main__":
    result = monte_carlo_game()
    print(f"Кількість ігор: {result['n_games']}")
    print(f"Кількість виграшів: {result['n_wins']}")
    print(f"Ймовірність виграшу: {result['p_win']:.6f}")
    print(f"Сумарний прибуток: {result['total_profit']}")
    print(f"Середній прибуток за гру: {result['avg_profit_per_game']:.6f}")
    print(f"Справедлива сума винагороди: {result['fair_reward']:.2f}")
    if result['avg_profit_per_game'] > 0:
        print("Гра вигідна для гравця.")
    elif result['avg_profit_per_game'] < 0:
        print("Гра невигідна для гравця.")
    else:
        print("Гра чесна.")



