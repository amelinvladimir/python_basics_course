# практические примеры

def check_access(func):
    def wrapper(*args, **kwargs):
        print("Проверка прав доступа")
        return func(*args, **kwargs)
    return wrapper

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана")
        return func(*args, **kwargs)
    return wrapper

def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                print("Повторный запуск")
        raise
    return wrapper

@check_access
@log_calls
@retry
def greet():
    print('Hello')

greet()