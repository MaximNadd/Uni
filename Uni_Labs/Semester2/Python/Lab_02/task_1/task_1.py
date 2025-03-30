# Задание 1: Работа с файлами
# Создайте текстовый файл data.txt и запишите в него 10 строк с произвольными числами (по одному числу в строке).

# Напишите программу, которая:

# - Читает числа из файла data.txt.

# - Вычисляет сумму, среднее арифметическое, максимальное и минимальное значение.

# - Записывает результаты в новый файл result.txt в формате:

# Сумма: [сумма]
# Среднее: [среднее]
# Максимум: [максимум]
# Минимум: [минимум]


file = open('task_1/data.txt', 'r')

numbers = [int(line.strip()) for line in file]

sum = sum(numbers)
average = sum / len(numbers)
max_number = max(numbers)
min_number = min(numbers)

with open('task_1/result.txt', 'w') as file:
    file.write(f"Sum: {sum}\n") 
    file.write(f"Average: {average}\n")         
    file.write(f"Max: {max_number}\n")
    file.write(f"Min: {min_number}\n")