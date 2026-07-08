# Использование @wraps(func) - крайне важно

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet():
    '''текст'''
    print('Привет')

print(greet.__name__)

greet()