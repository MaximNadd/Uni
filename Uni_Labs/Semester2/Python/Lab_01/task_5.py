# Задание 5: Дополнительное (по желанию)
# 1. Напишите программу, которая генерирует список из 20 случайных чисел от 1 до 100.
# 2. Выведите:
# - Все чётные числа из списка.
# - Все числа, которые делятся на 3.
# - Среднее арифметическое всех чисел в списке.

import random

numbers = [random.randint(1, 100) for _ in range(20)]
print(numbers)

print("\n")

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

print("\n")

divisible_by_3 = [num for num in numbers if num % 3 == 0]
print(divisible_by_3)

print("\n")

average = sum(numbers) / len(numbers)
print(average)