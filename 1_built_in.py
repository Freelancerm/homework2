#Створення функції
def my_sum() -> str:
    """Виводить повідомлення"""
    return "This is my custom sum function!"


#Перекриття вбудованої функції sum функцією my_sum
sum = my_sum()
"""Створення списку чисел"""
list_of_numbers = [1, 2, 3]
"""Виклик вбудованої функції sum, яка перекрита та вивід результату у консоль"""
print(__builtins__.sum(list_of_numbers))
"""Виклик функції my_sum та вивід результату у консоль"""
print(my_sum())
"""Виклик вбудованої функції sum, яка перекрита та вивід результату у консоль"""
print(__builtins__.sum(list_of_numbers))
