def make_counter():
    count = 0  # Состояние, которое мы хотим сохранить

    def counter():
        nonlocal count  # Говорим Python: "Используй переменную count из внешней функции!"
        count += 1
        return count

    return counter


# Создаем два независимых счетчика
counter_a = make_counter()
counter_b = make_counter()

print(counter_a())  # 1
print(counter_a())  # 2
print(counter_b())  # 1 (у него свое собственное замыкание!)
print(counter_a())  # 3
