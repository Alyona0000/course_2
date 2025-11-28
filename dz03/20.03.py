# окрім пункл д 
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# ФУНКЦІЯ Лагранжа
# =====================================================
def lagrange_interpolation(x_vals, y_vals, x):
    """
    x_vals — масив вузлів інтерполяції
    y_vals — значення функції в цих точках
    x — точка або масив точок, де обчислюємо P(x)
    """
    x = np.array(x)
    n = len(x_vals)
    P = np.zeros_like(x, dtype=float)

    for k in range(n):
        # L_k(x)
        Lk = np.ones_like(x, dtype=float)
        for i in range(n):
            if i != k:
                Lk *= (x - x_vals[i]) / (x_vals[k] - x_vals[i])

        P += y_vals[k] * Lk

    return P


# =====================================================
# ПРИКЛАД ДАНИХ  (сюди ставиш свої точки!)
# =====================================================
x_nodes = np.array([0, 1, 2, 3])
y_nodes = np.array([1, 2, 0, 4])

# =====================================================
# Будуємо сам поліном на проміжку
# =====================================================
x_plot = np.linspace(min(x_nodes), max(x_nodes), 500)
y_plot = lagrange_interpolation(x_nodes, y_nodes, x_plot)

# =====================================================
# Графік
# =====================================================
plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label="Інтерполяційний поліном Лагранжа", color='blue')
plt.scatter(x_nodes, y_nodes, color="red", label="Вузли інтерполяції", zorder=5)
plt.grid(True)
plt.legend()
plt.title("Інтерполяція поліномом Лагранжа")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()
