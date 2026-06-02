# Метод, изменяющий значение свойства


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"С днем рождения! Тебе теперь {self.age}")


p1 = Person("Линус", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
