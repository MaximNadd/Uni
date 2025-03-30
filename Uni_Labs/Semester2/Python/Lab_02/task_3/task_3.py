# Задание 3: Модули
# Создайте модуль math_operations.py, который содержит функции:

# add(a, b) — возвращает сумму двух чисел.

# subtract(a, b) — возвращает разность двух чисел.

# multiply(a, b) — возвращает произведение двух чисел.

# divide(a, b) — возвращает результат деления двух чисел (с обработкой деления на ноль).

# Продемонстрируйте работу данного модуля. (В другов файле сделать import math_operations)


import math_operations as mo

a = int(input("Введите числа : "))
b = int(input("Введите числа : "))

print(mo.add(a, b))
print(mo.subtract(a, b))
print(mo.multiply(a, b))
print(mo.divide(a, b))