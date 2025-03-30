# Задание 6: Дополнительное (по желанию)
# Напишите программу, которая:

# - Читает текстовый файл text.txt.

# - Используя регулярные выражения, находит все даты в формате DD.MM.YYYY.

# - Преобразует найденные даты в формат YYYY-MM-DD.

# - Сохраняет результат в файл dates.txt.

# - Используя лямбда-функции, отсортируйте даты по возрастанию и выведите их.

import re

def convert_date(date):
    day, month, year = map(int, date.split('.'))
    return f"{year}-{month:02d}-{day:02d}"

with open('task_6/text.txt', 'r') as file:
    text = file.read()

    dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)

    dates =  [convert_date(i) for i in dates]

    with open('task_6/dates.txt', 'w') as dates_file:
        dates_file.write('\n'.join(dates[::-1]))


sorted_dates = sorted(dates, key=lambda date: date)
print(sorted_dates)