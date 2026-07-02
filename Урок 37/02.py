def outer_function(name: str):
    # Это переменная во "внешней" области видимости
    greeting = f"Привет, {name}!"

    def inner_function():
        # Внутренняя функция имеет доступ к переменной greeting
        print(greeting)

    return inner_function  # Возвращаем саму функцию, а не результат её вызова!


# Создаем замыкание
my_greeter = outer_function("Алексей")

# Вызываем его позже. Функция outer_function уже завершилась,
# но my_greeter "помнит" значение greeting!
my_greeter()  # Вывод: Привет, Алексей!
