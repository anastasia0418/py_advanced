import csv
import json
import yaml

# Реализовать скрипт для чтения/записи данных в формате csv;

with open('doc.csv', 'r') as file:
    reader = csv.reader(file)
    print('Чтение данных в формате csv:\n')
    for row in reader:
        print(row)

headers = ['Фамилия', 'Имя', 'возраст']
newinfo = [
    {'Фамилия': 'Соколов', 'Имя': 'Петр', 'возраст': '78'},
    {'Фамилия': 'Иванов', 'Имя': 'Иван', 'возраст': '46'},
    {'Фамилия': 'Семенов', 'Имя': 'Семен', 'возраст': '23'},
    {'Фамилия': 'Смирнов', 'Имя': 'Даниил', 'возраст': '18'},
]

with open('doc.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, headers, delimiter=';')
    for row in newinfo:
        writer.writerow(row)

# Реализовать скрипт для чтения/записи данных в формате json

info = [
    {'name': 'Kate', 'age': 12},
    {'name': 'Dan', 'age': 20},
    {'name': 'Peter', 'age': 18},
]
json.dumps(info)

with open('doc2.json', 'w') as file:
    json.dump(info, file, indent=4)

with open('doc2.json', 'r') as file:
    print('В формате json:\n', json.load(file))

# Реализовать скрипт для чтения/записи данных в формате yaml

data = {
    'name1': 'Igor',
    'name2': 'Vasya',
    'last name': ['Semenov',
                  'Petrov']
}

with open('doc3.yml', 'w') as file:
    yaml.dump(data, file, Dumper=yaml.Dumper)

with open('doc3.yml', 'r') as file:
    print('В формате yaml:\n', yaml.load(file, Loader=yaml.Loader))

# Реализовать скрипт для преобразования данных в формате csv в формат json

csvPath = 'doc.csv'
jsonPath = 'file.json'

convert = []
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile)
    for rows in csvReader:
        convert.append(rows)

with open(jsonPath, 'w') as jsonFile:
    jsonFile.write(json.dumps(convert, indent=4))

with open(jsonPath, 'r') as file:
    print('Преобразования из csv в json:\n ', json.load(file))

# Реализовать скрипт для преобразования данных в формате json в формат yaml

jsonPath = 'doc2.json'
yamlPath = 'file.yml'
convert2 = []

with open(jsonPath) as jsonFile:
    jsonReader = json.load(jsonFile)
    for rows in jsonReader:
        convert2.append(rows)

with open(yamlPath, 'w') as yamlFile:
    yaml.dump(convert2, yamlFile, Dumper=yaml.Dumper)

with open(yamlPath, 'r') as file:
    print('Преобразования из json в yaml: ', yaml.load(file, Loader=yaml.Loader))

# Реализовать скрипт для преобразования данных в формате csv в формат yaml

csvPath = 'doc.csv'
yamlPath2 = 'convert.yml'

convert3 = []
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile)
    for rows in csvReader:
        convert3.append(rows)

with open(yamlPath2, 'w') as yamlFile:
    yaml.dump(convert3, yamlFile, Dumper=yaml.Dumper)

with open(yamlPath2, 'r') as file:
    print('Преобразования из csv в yaml: ', yaml.load(file, Loader=yaml.Loader))
