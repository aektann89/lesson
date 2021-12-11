import re

while True:
    items = input('Введите строку: \n')

    if items == 'exit':
        break

    result = re.search(r'(\d+)(?=\d\1)', items)
    print(result.group())