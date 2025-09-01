#Створення глобальної змінної:
discount = 0.1


#Створення глобальної функції
def create_order(price: float) -> float:
    """
    Обчислює кінцеву ціну з урахуванням знижки

    Args: price (float): Ціна замовлення
    """
    # Обчислення знижки
    price_with_discount = price * (1 - discount)

    # Створення вкладеної функції
    def apply_additional_discount(additional_discount: float):
        """"
        Обчислює кінцеву ціну з урахуванням додаткової знижки

        Args: additional_discount (float): Розмір додаткової знижки %
        """
        # Використання nonlocal, щоб функція могла змінювати кінцеву ціну у вкладеній області видимості.
        nonlocal price_with_discount
        # Обчислення додаткової знижки
        price_with_discount = price_with_discount * (1 - additional_discount)
        # Вивід результату у консоль
        print(f"Застосовано додаткову знижку(5%) \nКінцева ціна: {price_with_discount:.2f} грн")
    # Відображає початкову ціну
    print(f"Початкова ціна: {price:.2f} грн")
    #Відображає ціну з початковою знижкою
    print(f"Ціна зі знижкою 10%: {price_with_discount:.2f} грн")
    #Завдання параметрів (розміру знижки) для нашої вкладеної функції
    apply_additional_discount(0.05)

    #Повернення ціни зі знижкою
    return price_with_discount

create_order(1000)
