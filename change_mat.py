import json

mat = []

with open('мат.txt', encoding='utf-8') as file:
    mat = file.readline().split(' ')

with open('mat.json', 'w',  encoding='utf-8') as jsn:
    json.dump(mat, jsn)