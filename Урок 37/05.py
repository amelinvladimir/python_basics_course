def multiply_by(factor: float):
    """Возвращает функцию, умножающую аргумент на factor."""

    def multiplier(value: float) -> float:
        return value * factor

    return multiplier


double = multiply_by(2.0)
triple = multiply_by(3.0)

print(double(10))  # 20.0
print(triple(10))  # 30.0
