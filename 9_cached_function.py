from typing import Callable, Any, Dict


def memorize(func: Callable) -> Callable:
    """
    Кешує результати викликів функції, щоб уникнути повторних обчислень

    Args:
        func: Функція, результати якої потрібно кешувати.

    Returns:
        func (Callable): Обгорнута функція, яка використовує кеш
    """
    cache: Dict[Any, Any] = {}

    def wrapper(*args) -> Any:
        if args in cache:
            print(f"Повернення кешованого результату для {args}")
            return cache[args]
        else:
            print(f"Обчислюємо результат для {args}.....")
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


# Приклад використання
@memorize  # Виклик декоратору для кешування
def factorial(n: int) -> int:
    """Рекурсивно обчислює факторіал числа"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


print("--- Тестування Факторіалу ---")
print(f"Факторіал 5: {factorial(5)}")
# Отримання кешованого результату
print(f"Факторіал 5 (повторно, кешований результат): {factorial(5)}")
print(f"Факторіал 3: {factorial(3)}")
print(f"Факторіал 6: {factorial(6)}")


@memorize
def fibonacci(n: int) -> int:
    """Рекурсивно обчислює n-не число Фібоначчі. """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n--- Тестування Фібоначчі ---")
print(f"Фібоначчі 10: {fibonacci(10)}")
print(f"Фібоначчі 12: {fibonacci(12)}")
