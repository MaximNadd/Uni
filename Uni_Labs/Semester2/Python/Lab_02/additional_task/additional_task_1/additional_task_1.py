# Дополнительная задача 1: "Анализ логов сервера"
# Описание задачи:
# У вас есть файл server_logs.txt, который содержит логи веб-сервера. Каждая строка лога имеет следующий формат:

# [дата] [время] [IP-адрес] [метод] [URL] [статус] [размер ответа]
# Пример строки:
# [2023-10-01] [12:34:56] [192.168.1.1] [GET] [/index.html] [200] [1024]

# Задание:

# Напишите программу, которая:

# - Читает файл server_logs.txt.

# - Используя регулярные выражения, извлекает данные из каждой строки лога.

# Подсчитывает:

# - Количество запросов с кодом статуса 200.

# - Общий объём данных, переданных сервером (сумма всех размеров ответов).

# - Количество уникальных IP-адресов.

# - Сохраняет результаты в файл log_analysis.txt.

# - Используя лямбда-функции, отсортируйте логи по дате и времени и выведите первые 10 записей.

import re

with open('additional_task/additional_task_1/server_logs.txt', 'r') as file:
    server_logs = file.read()

    server_log_format = r"\[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\] \[(.*?)\]"

    # Используем re.findall для поиска всех совпадений
    data = re.findall(server_log_format, server_logs)

    status_200_count = 0
    answers_sum = 0
    unique_ips = set()

    log_analysis = open('additional_task/additional_task_1/log_analysis.txt', 'w', encoding="utf-8")

    for entry in data:
        date, time, ip, method, url, status, size = entry
        print(f"Дата: {date}, Время: {time}, IP: {ip}, Метод: {method}, URL: {url}, Статус: {status}, Размер: {size}")

        if status == '200':
            status_200_count += 1

        answers_sum += int(size)
        unique_ips.add(ip)


    logs_sorted = sorted(data, key=lambda x: (x[0], x[1]), reverse=True)

    log_analysis.write(f"количество статусов 200: {status_200_count}\n")
    log_analysis.write(f"сумма всех размеров ответов: {answers_sum}\n")
    log_analysis.write(f"Количество уникальных IP: {len(unique_ips) - 1}\n")

    for log in logs_sorted[:10]:
        log_analysis.write(str(log))
        log_analysis.write('\n')

        



    

