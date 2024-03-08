import csv

with open('students.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for s in reader:
        if 'Хадаров Владимир' in s[1]:
            print(f'Ты получил: {s[-1]} за проект - {s[2]}')
            break