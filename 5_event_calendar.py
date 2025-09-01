from typing import Tuple, Callable

# Створення глобальної змінної у вигляді списку наших подій
events = []


# Створення глобальної функції для взаємодії з календарем
def create_event() -> Tuple[Callable[[str], None], Callable[[str], None], Callable[[], None]] :
    """
    Створює функції-обгортки для управління подіями, використовуючи замикання
    Ця функція повертає три вкладені функції, які працюють з глобальним списком `events`

    Returns:
        Tuple: Кортеж з функціями (add_event, delete_event, show_events)
    """

    # Створення вкладеної функії додавання подій
    def add_event_func(event: str) -> None:
        """Додає подію до глобального календаря"""
        global events
        events.append(event)
        print(f"Подію {event} успішно додано!")

    # Створення вкладеної функії видалення подій
    def delete_event_func(event: str) -> None:
        """Видаляє подію з глобального календаря, якщо вона існує"""
        global events
        if event in events:
            events.remove(event)
            print(f"Подію {event} успішно видалено!")
        else:
            print(f"Подію {event} не знайдено в календарі, спочатку додайте подію щоб її видалити")

    # Створення вкладеної функції перегляду майбутніх подій
    def show_events_func() -> None:
        """Виводить усі майбутні події з глобального календаря"""
        global events
        if events:
            print(f"Майбутні події: \n{events}")
        else:
            print("У календарі немає запланованих подій")

    #Повертає вкладені функції
    return add_event_func, delete_event_func, show_events_func


#Присвоюємо функції змінним з більш зрозумілими іменами
add_event, delete_event, show_events = create_event()

#Приклади використання функцій:
# Додаємо події
add_event("Урок Python в ITHillel")
add_event("Виконати домашнє завдання")
add_event("English speaking club")

# Показуємо поточний список подій
show_events()

# Видаляємо подію
delete_event("Виконати домашнє завдання")
delete_event("Зустріч зі старим другом")  # Ця подія не існує

# Показуємо оновлений список подій
show_events()
