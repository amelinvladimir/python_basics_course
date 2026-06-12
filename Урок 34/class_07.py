class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


p1 = Person("Emil", 30)

# Python так меняет имя private метода
print(p1._Person__age)  # Не рекомендовано!
