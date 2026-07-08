# тоже самое без @

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def greet():
    print("Привет!")

decorator = repeat(3)
greet = decorator(greet)



greet()