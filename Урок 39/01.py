# простой декоратор

def my_decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

def say_hello():
    print("Привет!")

say_hello = my_decorator(say_hello)
say_hello()
