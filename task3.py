import csv

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))
header = reader[0]
reader = reader[1:]

n = input()
while n != 'СТОП':
    flag = 1
    for s in reader:
        if s[0] == n:
            print(f'Проект № {s[2]} делал: {s[1].split()[1][0]}. {s[1].split()[0]} он(а) получил(а) оценку - {s[-1]}.')
            flag = 0
            break
    if flag:
        print('Ничего не найдено.')
    n = input()
