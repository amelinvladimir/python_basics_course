f = None
try:
    f = open('file.txt', 'r', encoding='utf-8')
    content = f.read()
    print(content)
except FileNotFoundError:
    print("❌ Файл не найден.")
except UnicodeDecodeError:
    print("❌ Ошибка кодировки.")
except PermissionError:
    print("❌ Нет прав на чтение файла")
except Exception as e:
    print(f"⚠️ Неожиданная ошибка: {e}")
finally:
    if f is not None:
        f.close()
        print("🔒 Файл закрыт.")