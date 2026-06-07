class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        # В Python также есть функция super(), которая позволяет дочернему классу наследовать все методы и свойства родительского класса
        super().__init__(fname, lname)

        # добавляем свойство в наследуемом классе
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
x.printname()
