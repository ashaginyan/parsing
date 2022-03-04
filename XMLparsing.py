import xml.etree.ElementTree as ET

# lxml

tree = ET.parse('simple.xml')
print(tree)

root = tree.getroot()
print(root.tag)

for child1 in root:
    print(child1.tag, child1.attrib, child1.text)

for child1 in root:
    for child2 in child1:
        print(child2.tag, child2.attrib, child2.text)

print(root[0][1].tag)

for name in root.iter('name'):
    print(name.text)

for food in root.findall('food'):
    name = food.find('name').text
    price = food.find('price').text
    print(f'{name}: {price}')

print('___________')

# X-PATH
for el in root.findall(".//name"):
    print(el.text)