# замеряем время выполнения функции

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start:.6f} сек")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Функция завершена")

slow_function()