import csv
import random
import string

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))
header = reader[0]
reader = reader[1:]

def gen_log(name):
    names = name.split()
    login = f'{names[0]}_{names[1][0]}{names[2][0]}'
    return login

def gen_password() -> str:
    '''
    Функция генерирует пароль
    :return: password (str)
    '''
    n = string.ascii_letters + string.digits
    password = ''.join([random.choice(n) for i in range(8)])
    return password

for s in reader:
    s.append(gen_log(s[1]))
    s.append(gen_password())

with open('students_password.csv', 'w', encoding='utf-8', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',')
    csvwriter.writerow(header)
    csvwriter.writerows(reader)