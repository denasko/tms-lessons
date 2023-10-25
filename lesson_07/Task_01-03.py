import json

with open('file_01.txt', 'w') as f:
    f.write('Hello world!')



f2 = open('file_02.txt')
print(f2.read())



data = {'name': 'Den', 'surname': 'aviz', 'old': '23'}

with open('file_03.json', 'w') as p:
    json.dump(data, p)
