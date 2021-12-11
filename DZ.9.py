import re

while True:
    items = input('Введите числовую строку для проверки: \n')

    if items == 'exit':
        break

    result = re.search(r'(\d+)(?=\d\1)', items)
    print(result.group())