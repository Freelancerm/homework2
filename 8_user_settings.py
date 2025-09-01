from typing import Dict, Any, Callable, Tuple


def create_user_settings() -> Tuple[Callable[[str, Any], None], Callable[[str], Any], Callable[[], Dict[str, Any]]]:
    """
    Створює систему для зберігання налаштувань користувача за допомогою замикання.

    Returns:
        Кортеж, що містить три функції:
        - set_setting(key, value): встановлює або оновлює налаштування.
        - get_setting(key): повертає значення налаштування за ключем.
        - get_all_settings(): повертає всі налаштування.
    """
    settings: Dict[str, Any] = {
        "theme": "Light",
        "language": "en",
        "notifications": True
    }

    def _set_setting(key: str, value: Any) -> None:
        """Встановлює або оновлює значення налаштування."""
        settings[key] = value
        print(f"Налаштування '{key}' оновлено на '{value}'")

    def _get_setting(key: str) -> Any:
        """Повертає значення налаштування за ключем. Повертає None, якщо ключ не знайдено."""
        return settings.get(key)

    def _get_all_settings() -> Dict[str, Any]:
        """Повертає словник з усіма поточними налаштуваннями."""
        return settings.copy()

    return _set_setting, _get_setting, _get_all_settings


# Приклад використання:
# Отримуємо функції для управління налаштуваннями
set_setting, get_setting, get_all_settings = create_user_settings()

print("Початкові налаштування")
print(get_all_settings())

print("\n--- Зміна налаштувань ---")
# Змінюємо налаштування мови та теми
set_setting("language", "ua")
set_setting("theme", "dark")
#Додамо нове налаштування
set_setting("font_size", "small")

print("\n--- Перегляд окремих налаштувань ---")
# Переглядаємо окремі налаштування
print(f"Поточна мова: {get_setting('language')}")
print(f"Поточна тема: {get_setting('theme')}")
print(f"Налаштування, якого немає: {get_setting('invalid_key')}")

print("\n--- Перегляд всіх налаштувань ---")
# Переглядаємо всі налаштування після змін
print(f"Оновлені налаштування \n{get_all_settings()}")