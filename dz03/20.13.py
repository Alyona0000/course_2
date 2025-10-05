#Т20.13 Задані координати n точок на площині (x1,y1),...,(xn,yn). Знайти номери
#двох точок, відстань між якими найбільша (вважати, що така пара точок
#єдина), та саму відстань.
#Використати масиви numpy. Точки розмістити у двовимірному масиві 2xn.
#Побудувати тривимірний масив усіх можливих пар точок. Для побудови
#використати індексні масиви. Описати векторизовану функцію, яка обчислює
#відстань між 2 точками.




import numpy as np

def distance(p1, p2):
    """Векторизована функція для обчислення відстані між двома точками."""
    return np.sqrt(np.sum((p1 - p2) ** 2, axis=-1))

def find_farthest_points(points):
    """
    points: 2 x n numpy array, де points[0] - x, points[1] - y
    Повертає (i, j, max_dist): індекси точок та максимальна відстань
    """
    n = points.shape[1]
    # Індекси всіх пар (верхній трикутник, щоб не дублювати)
    idx1, idx2 = np.triu_indices(n, k=1)

    # Формуємо 3D масив пар точок: (кількість_пар, 2 точки, 2 координати)
    pairs = np.stack([points[:, idx1].T, points[:, idx2].T], axis=1)
    # pairs.shape == (num_pairs, 2, 2)

    # Обчислюємо відстані для всіх пар
    dists = distance(pairs[:,0,:], pairs[:,1,:])

    # Знаходимо найбільшу
    max_idx = np.argmax(dists)
    i, j = idx1[max_idx], idx2[max_idx]

    return i, j, dists[max_idx], pairs


if __name__ == "__main__":
    # Приклад: 5 точок
    points = np.array([
        [0, 1, 2, 3, 4],
        [0, 2, 1, 3, 0]
    ])  # shape: 2 x n

    i, j, max_dist, pairs = find_farthest_points(points)

    print(f"Найвіддаленіші точки: {i} та {j}")
    print(f"Відстань між ними: {max_dist:.4f}")
    print(f"Координати: {points[:,i]} та {points[:,j]}")

    print("\nПриклад тривимірного масиву пар точок:")
    print(pairs[:5])  # виведемо перші 5 пар
