import requests

r = requests.post('http://127.0.0.1:5000/post', json={'text': 'HELLO'})
print(r.json())

"""
1. Необходимо перейти на сайт с документами РЖД https://company.rzd.ru/ru/9353/page/105104?id=1794, 
 с помощью Selenium перейти по всем документах на их страницы, выпарсить тексты документов,
 выделить все организации в документах и представить результат в формате 1 GET-запроса REST API.
"""

