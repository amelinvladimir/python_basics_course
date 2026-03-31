# math_utils.py

PI = 3.14159

def add(a, b):
    print(f"__name__ в math_utls: {__name__}")
    return a + b

def multiply(a, b):
    return a * b

# Плохая практика: код выполняется при импорте!
# print("Модуль загружен!") 


# Этот код сработает ТОЛЬКО если запустить math_utils.py напрямую
if __name__ == "__main__":
    print("Запуск тестов модуля...")
    print(add(2, 2)) 