# Создадим класс с именем Person, свойствами firstname и lastname и методом printname

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


# Создаем класс с именем Student, который будет наследовать свойства и методы класса Person

class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()
