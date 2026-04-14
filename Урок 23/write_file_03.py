# Перезапись (w стирает старое содержимое!)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")  # \n нужно добавлять вручную!

# Дозапись (a добавляет в конец)
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write("Третья строка\n")