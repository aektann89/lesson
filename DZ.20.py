import json

file_object = open('DPPBVV1U.json', 'r')
my_object = (file_object.read())
my_result = json.loads(my_object)

sum_runtime = 0
for obj in my_result['_embedded']['episodes']:
        sum_runtime += my_result['runtime']
print(f'Чтобы полностью посмотреть все эпизоды вы потратите', sum_runtime, 'минут')


for obj in my_result['_embedded']['episodes']:
        season = obj['season']
        series = obj['number']
        named = obj['name']
        link = obj['url']
        description = obj['summary']
        print(f'Сезон', season, 'Серия', series)
        print(f'Название -', named)
        print(f'Краткое описание серии...', description)
        print(f'Подробнее...', link)
