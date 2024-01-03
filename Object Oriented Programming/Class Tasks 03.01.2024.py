file = open('weather_data.csv')
data = []

for f in file.readlines():
    current_data = f.replace('\n', '')
    data.append(current_data)

print(data)

# List Comprehension Way
list_comprehension_data = [f.replace('\n', '') for f in file.readlines()]

# print(list_comprehension_data)

second_task_file = open('weather_data.csv')
second_task_data = []
for f in second_task_file.readlines():
    current_data = f.split(';')[1]
    if current_data.isdigit():
        second_task_data.append(int(current_data))
    else:
        second_task_data.append(current_data)

print(second_task_data)

# List Comprehension Way

comprehension_method = [int(f.split(';')[1]) if f.split(';')[1].isdigit() else f.split(';')[1] for f in second_task_file]

# print(comprehension_method)

import csv

with open('weather_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    temperatures = [[int(v.split(';')[1]) if v.split(';')[1].isdigit() else v.split(';')[1] for v in f][0] for f in data]
    print(temperatures)


# import pandas as pd
# data = pd.read_csv('weather_data.csv')
# data_dict = data.to_dict('temp')
# print(data_dict)
