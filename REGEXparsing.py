import re

# https://docs.python.org/3/library/re.html

pattern = re.compile('\d+ +руб.*\d+ +коп')

f = open('telegram.txt', 'r')
text = f.read()
f.close()
money = pattern.findall(text)
print(money)

s = '+7 (999) 899-55-33'

s2 = '+7943623 55 01'

p = re.compile('(\+7 \(\d{3}\) \d{3}-\d{2}-\d{2})')

print(p.findall(s))