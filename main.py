import csv

# Чтение данных из файла
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))
header = reader[0]
reader = reader[1:]
average_mark = 0
count_mark = 0
# Считаем среднюю оценку и выводим оценку за проект Хадарова Владимира
for s in reader:
    if s[-1] != 'None':
        average_mark += int(s[-1])
        count_mark += 1
    if 'Хадаров Владимир' in s[1]:
        print(f'Ты получил: {s[-1]} за проект - {s[2]}')
# m это среднее значение
m = "%.3f" % (average_mark / count_mark)
# Заменяем ошибки на среднее значение оценок
for s in reader:
    if s[-1] == 'None':
        s[-1] = m
# Записываем данные в новый файл
with open('student_new.csv', 'w', encoding='utf-8', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',')
    csvwriter.writerow(header)
    csvwriter.writerows(reader)