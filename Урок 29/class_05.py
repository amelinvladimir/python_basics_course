# Вы также можете вызывать методы внутри класса с помощью self


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")


p1 = Person("Tobias")
p1.welcome()
