# Задание 4: Работа со списками
# 1. Создайте список из 10 случайных чисел (можно использовать модуль random или ввести числа вручную).
# 2. Выполните следующие действия:
# - Выведите список.
# - Найдите и выведите максимальное и минимальное значение в списке.
# - Вычислите и выведите сумму всех элементов списка.
# - Отсортируйте список по возрастанию и выведите его.

import random

numbers = [random.randint(0, 100) for _ in range(10)]
print(numbers)

print("maximum number = %d" % max(numbers))
print("minimum number = %d" % min(numbers))
print("sum = %d" % sum(numbers))

numbers.sort()
print(numbers)