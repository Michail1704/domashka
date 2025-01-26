
import json

file_name = 'input.json'
with open(file_name) as file:
    data = json.load(file)


def task(data_json) -> float:
    summ = 0
    for i in data_json:
        summ += float(i["weight"]) * float(i["score"])
    return summ


print(f'{task(data):.3f}')