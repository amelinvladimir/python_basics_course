filename = 'file.txt'

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"Прочитано {len(lines)} строк.")
except FileNotFoundError:
    print(f"❌ Файл '{filename}' не найден.")
except PermissionError:
    print(f"❌ Нет прав на чтение файла '{filename}'.")
except UnicodeDecodeError:
    print(f"❌ Ошибка кодировки. Попробуйте другую или проверьте файл.")
else:
    print("✅ Чтение прошло успешно.")
finally:
    print("🔒 Операция с файлом завершена.")