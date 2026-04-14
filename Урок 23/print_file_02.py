# Вариант 1: весь файл в одну строку
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Вариант 2: построчно (экономит память, лучше для больших файлов)
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # strip() убирает \n и пробелы по краям
        
# Вариант 3: построчно
with open('file.txt', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()
        if content == '':
            break
        print(content.strip())
        
# Вариант 4: определенное количество символов
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read(12)
    print(content)