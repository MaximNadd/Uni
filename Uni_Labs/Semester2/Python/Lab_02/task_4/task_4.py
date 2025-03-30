# Задание 4: Регулярные выражения
# Напишите программу, которая:

# - Читает текстовый файл text.txt.

# Используя регулярные выражения, находит и выводит:

# - Все email-адреса.

# - Все номера телефонов в формате +7-XXX-XXX-XX-XX.

# - Все слова, начинающиеся с заглавной буквы.

# - Сохраните результаты в отдельные файлы (emails.txt, phones.txt, capital_words.txt).

import re

with open('task_4/text.txt', 'r') as file:
    text = file.read()

    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phones = re.findall(r'\+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', text)
    capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)

    with open('task_4/emails.txt', 'w') as emails_file:
        emails_file.write('\n'.join(emails))

    with open('task_4/phones.txt', 'w') as phones_file:
        phones_file.write('\n'.join(phones))

    with open('task_4/capital_words.txt', 'w') as capital_words_file:
        capital_words_file.write('\n'.join(capital_words))