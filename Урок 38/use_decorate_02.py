from functools import cache

@cache
def fibonacci(n):
    print(f"Вычисляю fibonacci({n})")

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(8))
