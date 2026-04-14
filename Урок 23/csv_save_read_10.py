import csv

def read_csv_safely(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
        if not data:
            print("⚠️ Файл пуст или содержит только заголовок.")
            return []
            
        print(f"✅ Успешно прочитано {len(data)} записей.")
        
    except FileNotFoundError:
        print(f"❌ Файл '{filepath}' не найден.")
    except csv.Error as e:
        print(f"🔍 Ошибка структуры CSV: {e}")
    except UnicodeDecodeError:
        print("❌ Неверная кодировка. Файл не в UTF-8.")
    except PermissionError:
        print(f"❌ Нет прав на чтение файла '{filepath}'.")
    finally:
        print("🔒 Операция завершена.")

# Использование
read_csv_safely('users.csv')