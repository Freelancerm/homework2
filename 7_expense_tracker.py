# Створення глобальної змінної для відстеження глобальної сумми витрати
total_expense: float = 0.0


def add_expense(expense: float) -> None:
    """
    Додає суму витрат до загальної суми

    Args: expense (float) : Сума яку потрібно додати

    """
    global total_expense
    if expense >= 0:
        total_expense += expense
        print(f"Успішно додано {expense:.2f} грн.")
    else:
        print("Будь ласка, введіть додатнє число")


def get_expense():
    """Повертає значення загальної суми витрат"""
    return total_expense


def show_menu() -> None:
    """Відображає меню"""
    print("Будь ласка, виберіть дію зі списку:")
    print(" 1. Додати витрати")
    print(" 2. Переглянути загальну суму")
    print(" 3. Вийти")


def main_menu() -> None:
    """Дозволяє користувачу обрати пункт меню та виконати відповідну дію"""
    print("Ласкаво просимо до вашого трекера витрат!")

    while True:
        show_menu()
        user_choice = input("Ваш вибір: ")

        if user_choice == "1":
            try:
                expense = float(input("Введіть суму витрат: "))
                """Виклик нашої функції для додавання суми до наших витрат"""
                add_expense(expense)
            except ValueError:
                print("Не коректний ввід. Будь ласка введіть число")
        elif user_choice == "2":
            print(f"Загальні витрати {get_expense():.2f} грн.")
        elif user_choice == "3":
            print(f"\nДякуємо за використання! Ваш остаточний підсумок: {get_expense():.2f} грн.")
            break
        else:
            print("Неправильний вибір. Будь ласка, оберіть номер зі списку.")


# Виклик головної програми, а саме нашого меню
if __name__ == "__main__":
    main_menu()
