def make_withdraw(balance: float):
    """Создает функцию для снятия денег с проверкой баланса."""

    def withdraw(amount: float) -> float:
        nonlocal balance
        if amount > balance:
            raise ValueError("Недостаточно средств")
        balance -= amount
        return balance

    return withdraw


my_account = make_withdraw(100.0)
print(my_account(30.0))  # 70.0
print(my_account(50.0))  # 20.0
# print(my_account(30.0)) # Вызовет ValueError
