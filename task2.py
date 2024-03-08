n = [0, 7, 8, 4, 3, 1, 10]
'''
for i in range(1, len(n)):
    j = i
    while n[j] < n[j - 1] and j > 0:
        n[j], n[j - 1] = n[j - 1], n[j]
        j -= 1
'''
'''
for i in range(len(n) - 1):
    m = max(n)
    k = 0
    for j in range(i, len(n)):
        if n[j] < m:
            m = n[j]
            k = j
    n[i], n[k] = n[k], n[i]
print(n)
'''

import csv

# Чтение данных из файла
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))
header = reader[0]
reader = reader[1:]
for i in range(1, len(reader)):
    j = i
    while reader[j][-1] < reader[j - 1][-1] and j > 0:
        reader[j], reader[j - 1] = reader[j - 1], reader[j]
        j -= 1
print('10 класс:')
i = 1
for s in reader:
    if s[-1] == '5' and '10' in s[-2]:
        print(f'{i} место: {s[1].split()[1][0]}. {s[1].split()[0]}')
        i += 1
    if i == 4:
        break