# Данные: счета представлены словарями
account1 = {"owner": "Анна", "balance": 1000, "currency": "RUB", "email": "anna@example.com"}
account2 = {"owner": "Борис", "balance": 500, "currency": "RUB", "email": "boris@example.com"}
account3 = {"owner": "Виктор", "balance": 200, "currency": "USD", "email": "victor@example.com"}

# Общая функция отправки оповещения
def send_notification(account, operation_type, amount, new_balance):
    message = f"[ОПОВЕЩЕНИЕ] для {account['owner']} ({account['email']}): "
    message += f"Операция: {operation_type}, сумма: {amount} {account['currency']}, "
    message += f"баланс: {new_balance} {account['currency']}"
    print(message)

# ОБЩАЯ ФУНКЦИЯ ИЗМЕНЕНИЯ БАЛАНСА (теперь единая!)
def update_balance(account, delta, operation_type):
    """Изменяет баланс счета и отправляет оповещение"""
    old_balance = account["balance"]
    new_balance = old_balance + delta
    account["balance"] = new_balance
    send_notification(account, operation_type, abs(delta), new_balance)
    return new_balance

# Функции операций (теперь очень короткие)
def deposit(account, amount):
    if amount > 0:
        update_balance(account, amount, "пополнение")
        print(f"OK: +{amount} {account['currency']}")
    else:
        print("Ошибка: сумма должна быть положительной")

def withdraw(account, amount):
    if amount > 0 and account["balance"] >= amount:
        update_balance(account, -amount, "снятие")
        print(f"OK: -{amount} {account['currency']}")
    else:
        print("Ошибка: недостаточно средств или неверная сумма")

def transfer(from_account, to_account, amount):
    if from_account["currency"] != to_account["currency"]:
        print("Ошибка: разные валюты, перевод невозможен")
        return
    if from_account["balance"] >= amount:
        # Используем общую функцию для списания
        update_balance(from_account, -amount, "перевод (отправка)")
        # Используем общую функцию для зачисления
        update_balance(to_account, amount, "перевод (получение)")
        print(f"Переведено {amount} {from_account['currency']}")
    else:
        print("Ошибка: недостаточно средств")

def show_account(account):
    print(f"{account['owner']}: {account['balance']} {account['currency']}")

# Использование
show_account(account1)
deposit(account1, 300)
withdraw(account1, 100)
transfer(account1, account2, 200)
show_account(account1)
show_account(account2)