import json

file = open('simple.json', 'r')
d = json.load(file)
print(type(d))
print(d['breakfast_menu']['food3']['price'])
file.close()