# ""
# Задание 1: Условные операторы
# 1. Напишите программу, которая запрашивает у пользователя три числа.

# 2. Определите и выведите:
# - Наибольшее из трёх чисел.
# - Наименьшее из трёх чисел.
# - Являются ли все числа равными.


input_numbers = input("Введите три числа через пробел: ").split()

input_numbers = [int(num) for num in input_numbers]

print(max(input_numbers))
print(min(input_numbers))
print(input_numbers[0] == input_numbers[1] == input_numbers[2])

