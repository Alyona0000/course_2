#На домашнє завдання: Т19.6, Т19.7
#Зауваження! Декоратори можете застосовувати до тих класів, які уже у вас є (не обов"язково ті що у завданні)

#Т19.6 Описати декоратор класу, який здійснює модифікацію класу з метою
#трасування виклику усіх власних (не спеціальних) методів класу. Під час
#трасування показувати ім’я методу, значення параметрів до виклику, а також
#результат після виклику. Застосувати цей декоратор до класів Person та
#Student (див. тему «Класи та об’єкти») та виконати програму обчислення
#стипендії студентам.





def trace_methods(cls):
    #Декоратор класу для трасування викликів усіх власних (не спеціальних) методів.
    import functools

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):

            # робимо фабрику-обгортку, щоб уникнути проблем із замиканням
            def make_wrapper(method):
                @functools.wraps(method)
                def wrapper(self, *args, **kwargs):
                    print(f"Виклик {cls.__name__}.{method.__name__} з args={args}, kwargs={kwargs}")
                    result = method(self, *args, **kwargs)
                    print(f"Результат {cls.__name__}.{method.__name__}: {result}")
                    return result
                return wrapper

            setattr(cls, attr_name, make_wrapper(attr_value))

    return cls


@trace_methods
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


@trace_methods
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def calc_scholarship(self):
        if self.grade >= 90:
            return 2000
        elif self.grade >= 75:
            return 1200
        else:
            return 0


# Перевірка роботи
if __name__ == "__main__":
    s = Student("Іван", 92)
    print("Ім'я:", s.get_name())
    print("Оцінка:", s.get_grade())
    print("Стипендія:", s.calc_scholarship())
