# Створення глобальної змінної
default_time = 60


# Створення функції
def training_session(rounds: int) -> None:
    """
    Приймає кількість раундів тренування
    Використовує змінну що відповідає за час та раунд і локально змінює її для кожного тренування

    Args: rounds (int) : Кількість раундів
    Returns: time_per_round (int) : Час для кожного раунду
    """
    time_per_round = default_time

    # Створення вкладеної функції
    def adjust_time():
        """
        Налаштовує час для кожного окремого раунду
        """
        # Неявне використання nonlocal
        nonlocal time_per_round
        # Віднімаємо 5 хвилин для кожного наступного раунду
        time_per_round -= 5
        return time_per_round

    # Використовуємо цикл для виведення тривалості кожного раунду
    for i in range(1, rounds + 1):
        if i == 1:
            print(f"Раунд {i}: {time_per_round} хвилин")
        else:
            current_time = adjust_time()
            print(f"Раунд {i}: {current_time} хвилин (після коригування часу)")


#Приклад використання
training_session(10)
