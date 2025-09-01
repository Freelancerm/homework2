from typing import Callable, Union


# Створення функції
def create_calculator(operator: str) -> Callable[[Union[int, float], Union[int, float]], Union[int, float, str]]:
    """
    Створює функцію-калькулятор для заданого оператора

    Args: operator (str) : Рядок, що представляє собою математичну дію ('+', '-', '*', '/")

    Returns:
        Callable: Функція, яка приймає два числа та повертає результат обчислення.
                  У випадку помилки повертає рядок з повідомленням про неї.
    """

    # Створення вкладеної функції
    def calculator(x: float, y: float):
        """
        Вкладена функція яка виконує обчислення

        Args: x (float), y (float) : приймає числа з якими потрібно виконати дію

        Returns:
             Повертає резутат виконаної дії
        """
        if operator == "+":
            return x + y
        elif operator == "-":
            return x - y
        elif operator == "*":
            return x * y
        elif operator == "/":
            if y == 0:
                return "Помилка: Ділення на нуль неможливе!"
            return x / y
        else:
            return f"Помилка: Непідтримуваний оператор '{operator}'"

    return calculator


# Створюємо калькулятори для різних операцій
add = create_calculator('+')
subtract = create_calculator('-')
multiply = create_calculator('*')
divide = create_calculator('/')
power = create_calculator('**') # Непідтримуваний оператор

# Тестуємо калькулятори
print(f"5 + 3 = {add(10, 93)}")
print(f"10 - 4 = {subtract(120, 33)}")
print(f"2 * 7 = {multiply(2, 4)}")
print(f"15 / 3 = {divide(17, 2)}")
print(f"8 / 0 = {divide(9, 0)}")
print(f"2 ** 3 = {power(6, 3)}")
