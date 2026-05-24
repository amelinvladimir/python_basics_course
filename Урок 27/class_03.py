class MyClass:
    """Простой пример класса"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
print(x.i)
print(x.f())

del x