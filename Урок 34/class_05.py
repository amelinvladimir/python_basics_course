class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected свойство


p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)  # Доступ есть, но по соглашению не обращаемся