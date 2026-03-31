def to_upper(text):
    while True:
        try:
            s = input("Введите число: ")
            i = int(s)
            print(i)
        except NameError:
            print("x не найден")
        finally:
            print("Закрываем все подключения")

        break

    return text.upper()


def to_lower(text):
    return text.lower()


to_upper("aaa")