import json

file = open('Test.ipynb', 'r')
d = json.load(file)
# print(d)

print(d['cells'][1]['outputs'])

d['cells'][3]['outputs'] = [{'data': {'text/plain': ['3.1415']}, 'execution_count': 3, 'metadata': {}, 'output_type': 'execute_result'}]
file.close()

file = open('Test.ipynb', 'w')
json.dump(d, file)
file.close()