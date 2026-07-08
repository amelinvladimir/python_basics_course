# декорирование функции, принимающей аргументы

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(2, 3))