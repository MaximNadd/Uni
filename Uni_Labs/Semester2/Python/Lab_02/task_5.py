# Задание 5: Лямбда-функции
# - Создайте список чисел от 1 до 20.

# Используя лямбда-функции и функции высшего порядка, выполните следующие действия:

# - Отфильтруйте список, оставив только чётные числа.

# - Увеличьте каждое число в списке на 10.

# - Отсортируйте список по убыванию.

# - Выведите результаты.

numbers = list(range(1, 21))

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

increased_numbers = list(map(lambda x: x + 10, filtered_numbers))
print(increased_numbers)

sorted_numbers = sorted(increased_numbers, reverse=True)
print(sorted_numbers)