# Из класса метод можно удалить


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")


p1 = Person("Emil")

del Person.greet

p1.greet()  # Ошибка
