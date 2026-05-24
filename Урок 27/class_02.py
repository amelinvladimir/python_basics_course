class MyClass:
    """Простой пример класса"""
    i = 12345

    def f(self):
        return 'hello world'
    
    
print(MyClass.i)

MyClass.i = 5
print(MyClass.i) 