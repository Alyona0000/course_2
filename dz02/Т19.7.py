#На домашнє завдання: Т19.6, Т19.7
#Зауваження! Декоратори можете застосовувати до тих класів, які уже у вас є (не обов"язково ті що у завданні)

#Т19.7 Описати декоратор класу, який здійснює модифікацію класу з метою
#обчислення часу роботи усіх методів класу. Під час виклику методу
#показувати ім’я методу та час його роботи. Застосувати цей декоратор до
#класу Btree (див. приклад до теми «Рекурсивні структури даних») та
#побудувати бінарне дерево пошуку.


import time
import functools

def time_methods(cls):
    #Декоратор класу для вимірювання часу виконання всіх власних (не спеціальних) методів класу.

    def make_wrapper(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            start = time.perf_counter()
            result = method(self, *args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"Метод {cls.__name__}.{method.__name__} виконувався {elapsed:.6f} сек.")
            return result
        return wrapper

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, make_wrapper(attr_value))

    return cls


# Простий приклад класу Btree для демонстрації
@time_methods
class Btree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Btree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Btree(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()


# Перевірка роботи
if __name__ == "__main__":
    print("\n--- Btree demo ---")
    tree = Btree(10)
    for v in [5, 15, 3, 7, 12, 18]:
        tree.insert(v)
    print("Inorder traversal:", end=" ")
    tree.inorder()
    print()
