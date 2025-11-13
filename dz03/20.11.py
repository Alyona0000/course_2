# Т20.11 Скласти програму, що перевіряє чи є задана квадратна матриця з
#цілих чисел магічним квадратом, тобто такою, в якій суми елементів в усіх
#рядках і стовпчиках однакові.
#Використати масиви numpy та векторизувати програмний код.

import numpy as np

def is_magic_square(matrix):
    matrix = np.array(matrix)
    n, m = matrix.shape
    if n != m:
        return False  # Не квадратна матриця

    target_sum = np.sum(matrix[0, :]) #  15
    row_sums = np.sum(matrix, axis=1) #  [7, 9, 5]
    col_sums = np.sum(matrix, axis=0)

    if not (np.all(row_sums == target_sum) and np.all(col_sums == target_sum)):
        return False

    # Додатково можна перевірити діагоналі (якщо потрібно для "повного" магічного квадрату)
    # diag1 = np.sum(np.diag(matrix))
    # diag2 = np.sum(np.diag(np.fliplr(matrix)))
    # if not (diag1 == target_sum and diag2 == target_sum):
    #     return False

    return True

if __name__ == "__main__":
    # Приклад магічного квадрату 3x3
    mat = np.array([
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ])
    print("Магічний квадрат:" if is_magic_square(mat) else "Не магічний квадрат")

    # Не магічний квадрат
    mat2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Магічний квадрат:" if is_magic_square(mat2) else "Не магічний квадрат")


