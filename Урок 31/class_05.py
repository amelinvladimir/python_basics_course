# Метод __str__() — это специальный метод, который определяет, что будет выведено при выводе объекта на экран

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person1("Emil", 36)
print(p1)


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


p1 = Person2("Tobias", 36)
print(p1)
