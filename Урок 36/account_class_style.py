class EmailNotifier:
    def send(self, account, operation_type, amount):
        print(f"[EMAIL] {account.email}: {operation_type} {amount}")

class PushNotifier:
    def send(self, account, operation_type, amount):
        print(f"[PUSH] {account.owner}: {operation_type} {amount}")

class Account:
    def __init__(self, owner, balance, currency, email, notifier=None):
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.email = email
        self.notifier = notifier or EmailNotifier()  # по умолчанию email
    
    def _send_notification(self, operation_type, amount):
        if self.notifier:
            self.notifier.send(self, operation_type, amount)
    
    def _update_balance(self, amount, operation_type):
        """Общая логика изменения баланса с оповещением"""
        self.balance += amount
        self._send_notification(operation_type, abs(amount))
    
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount, "пополнение")
            print(f"OK: +{amount} {self.currency}")
        else:
            print("Ошибка: сумма должна быть положительной")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self._update_balance(-amount, "снятие")
            print(f"OK: -{amount} {self.currency}")
        else:
            print("Ошибка: недостаточно средств или неверная сумма")
    
    def transfer(self, to_account, amount):
        if self.currency != to_account.currency:
            print("Ошибка: разные валюты")
            return
        if self.balance >= amount:
            # Списание у отправителя
            self._update_balance(-amount, "перевод (отправка)")
            # Зачисление получателю
            to_account._update_balance(amount, "перевод (получение)")
            print(f"Переведено {amount} {self.currency}")
        else:
            print("Ошибка: недостаточно средств")
    
    def show(self):
        print(f"{self.owner}: {self.balance} {self.currency}")

# Использование
acc1 = Account("Анна", 1000, "RUB", "anna@example.com")
acc2 = Account("Борис", 500, "RUB", "boris@example.com")

acc1.show()
acc1.deposit(300)
acc1.withdraw(100)
acc1.transfer(acc2, 200)
acc1.show()
acc2.show()