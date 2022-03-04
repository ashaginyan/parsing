import requests
from bs4 import BeautifulSoup

base_url = 'https://www.gov.spb.ru'
url = 'https://www.gov.spb.ru/gov/otrasl/c_transport/'

r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
texts = soup.findAll('p')
for text in texts:
    print(text.text)

ulist = soup.find('ul', class_='sidemenu')
links = ulist.find_all('a')

for link in links:
    print(base_url + link['href'])

# Задание: перейти по всем ссылкам и собрать текст с каждой из страниц


r = requests.get('https://www.rzd.ru/')
print(r.text)