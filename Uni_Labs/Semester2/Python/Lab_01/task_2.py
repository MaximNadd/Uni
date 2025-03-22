# Задание 2: Цикл for
# 1. Напишите программу, которая запрашивает у пользователя число n.
# 2. Используя цикл for, выведите:
# - Все числа от 1 до n.
# - Квадраты чисел от 1 до n.
# - Сумму всех чисел от 1 до n.



n = int(input("Введите число: "))
for i in range(1, n + 1):
    print(i)

print("\n")

for i in range(1, n + 1):
    print(i * i)
sum = 0

print("\n")

for i in range(1, n + 1):
    sum += i
print(sum)