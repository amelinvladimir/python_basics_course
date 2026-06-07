class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


# Добавим __init__() функцию в Student класс
class Student(Person):
    def __init__(self, fname, lname, year):
        # Чтобы сохранить наследование родительской __init__() функции, добавим вызов родительской __init__() функции:
        Person.__init__(self, fname, lname)

        # Добавим свойство graduationyear в класс Student
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
x.printname()
