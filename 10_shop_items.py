from typing import Callable, Tuple


def create_product(name: str, price: float, quantity: int) -> Tuple[Callable[[float], None], Callable[[], str]]:
    """
    Створює об'єкт товару та повертає функцію для зміни його ціни.

    Args:
        name(str): Назва товару.
        price(float): Ціна товару.
        quantity(int): Кількість товару.

    Returns:
        Callable: Функція 'set price' для зміни ціни товару.
    """
    # Стан, який "замкнений" у функції
    _name = name
    _price = price
    _quantity = quantity

    def set_price(new_price: float) -> None:
        """
        Змінює ціну товару
        Це замикання, яке має доступ до _price з батьківської функції
        """
        nonlocal _price
        if new_price > 0:
            _price = new_price
            print(f"Ціну товару {_name} змінено на {_price:.2f} грн.")
        else:
            print("Введена ціна некоректна. Ціна повинна бути додатнім числом.")

    # Додаткові функції для демонстрації замикання
    def get_info() -> str:
        """Повертає інформацію про товар"""
        return f"Товар: {name}, Ціна: {_price:.2f} грн, Кількість: {_quantity} шт."

    # Повернення функції, яка дозволяє змінювати ціну
    return set_price, get_info


# Приклад
# Створюємо товар і отримуємо функції для змінення ціни
set_phone_price, get_phone_info = create_product("Телефон", 21000.00, 20)

# Початкова інформація про товар
print("--- Початкова інформація ---")
print(get_phone_info())

# Змінюємо ціну товару за допомогою замикання
print("\n--- Зміна ціни ---")
set_phone_price(19999.99)

# Спроба змінити ціну на некоректне значення
set_phone_price(-1000.00)

# Перевірка, як змінилась ціна на товар
print("\n--- Оновлена інформація ---")
print(get_phone_info())
