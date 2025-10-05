#Т20.15 Задані координати n точок на площині (x1,y1),...,(xn,yn). Знайти
#кількість рівносторонніх трикутників, утворених цими точками.

#Використати масиви numpy. Точки розмістити у двовимірному масиві 2xn.
#Побудувати тривимірний масив усіх можливих трійок точок. Для побудови
#використати індексні масиви. Описати векторизовану функцію, яка
#перевіряє, чи є трикутник, утворений 3 точками, рівностороннім.



import numpy as np

def distance(p1, p2):
    #Векторизовано обчислює відстань між двома точками (або масивами точок).
    return np.sqrt(np.sum((p1 - p2) ** 2, axis=-1))

def is_equilateral(triangles, tol=1e-8):
    #triangles: масив форми (num, 3, 2) - num трикутників, кожен з 3 точок по 2 координати
    #tol: допустима похибка для порівняння сторін
    #Повертає булевий масив: чи є трикутник рівностороннім
    
    a = distance(triangles[:, 0, :], triangles[:, 1, :])
    b = distance(triangles[:, 1, :], triangles[:, 2, :])
    c = distance(triangles[:, 2, :], triangles[:, 0, :])
    return (np.abs(a - b) < tol) & (np.abs(b - c) < tol) & (a > tol)

def count_equilateral_triangles(points):
    #points: 2 x n numpy array, де points[0] - x, points[1] - y
    #Повертає кількість рівносторонніх трикутників
    
    n = points.shape[1]
    # Усі унікальні трійки індексів
    idx = np.array(np.triu_indices(n, k=1)).T  # але це для пар
    # Краще скористатися itertools.combinations через numpy
    triples = np.array(list(itertools.combinations(range(n), 3)))

    # Формуємо масив трикутників: (num, 3, 2)
    triangles = np.stack([
        points[:, triples[:, 0]].T,
        points[:, triples[:, 1]].T,
        points[:, triples[:, 2]].T
    ], axis=1)

    eq_mask = is_equilateral(triangles)
    return np.sum(eq_mask)

if __name__ == "__main__":
    import itertools

    # Приклад: 5 точок, серед яких є рівносторонній трикутник
    points = np.array([
        [0, 1, 2, 0.5, 1.5],
        [0, 0, 0, np.sqrt(3)/2, np.sqrt(3)/2]
    ])  # shape: 2 x n

    count = count_equilateral_triangles(points)
    print(f"Кількість рівносторонніх трикутників: {count}")
