import json

data = [input('Enter name'), input('Enter surname'), input('Enter years old')]

with open('file_04.json', 'w') as file_04:
    json.dump(data, file_04)



with open('file_04.json') as file_04:
    print(json.load(file_04))
