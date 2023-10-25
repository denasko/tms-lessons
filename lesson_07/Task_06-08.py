import csv

header = ['name', 'surname', 'gender', 'old']
data = [('denasko', 'avizhonis', 'M', '23')]

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(header)
    for i in data:
        writer.writerow(i)



header = ['name', 'surname', 'gender']
data = [(input('Enter ypur name'), input('Enter your surname'),
         input('Enter your gender (M/F))'))]

with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    for i in data:
        writer.writerow(i)



with open('file_07.csv') as file_08:
    file_reader = csv.reader(file_08)
    next(file_reader)
    for i in file_reader:
        print(f'{i[0]} {i[1]} {i[2]}')
