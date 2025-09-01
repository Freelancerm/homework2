# Створення глобальної змінної
subscribers = []


#Створення глобальної функції:
def subscribe(name: str) -> None:
    """Додає ім'я підписника до глобального списку та підтверджує підписку

    Args:
        name (str): Ім'я підписника
    """
    # Додавання ім'я підписника
    subscribers.append(name)

    # Створення вкладеної функції
    def confirm_subscription() -> str:
        """Повертає повідомлення про підтвердження підписки"""
        return f'Підписка підтверджена для {name}'

    # Виклик вкладеної функції та виведення її результату у консоль
    print(confirm_subscription())


def unsubscribe(name: str) -> None:
    """Видаляє підписника з глобального списку

    Args:
        name (str): Ім'я підписника, яке потрібно видалити
    """
    if name in subscribers:
        subscribers.remove(name)
        print(f'{name} успішно відписаний')
    else:
        print(f'Підписника {name} для видалення не знайдено')


# Приклади використання
subscribe("Олена")
subscribe("Ігор")
subscribe("Володимир")
unsubscribe("Ігор")
unsubscribe("Арсеній")
# Перевіряємо список підписників після додавання
print(f'Поточний список підписників: {subscribers}')
