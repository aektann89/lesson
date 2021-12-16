length_in_meters = float(input('Введите значение в метрах: '))
def converter(length_in_meters, convert_type):
    if convert_type == 'sm':
        result = f'{(length_in_meters * 100)} сантиметров'
    elif convert_type == 'ft':
        result = f'{(length_in_meters * 3.281)} футов'
    elif convert_type == 'in':
        result = f'{(length_in_meters * 39.37)} дюймов'
    elif convert_type == 'sj':
        result = f'{(length_in_meters / 1.829)} саженей'
    return result

print(converter(length_in_meters, 'sm'))
print(converter(length_in_meters, 'ft'))
print(converter(length_in_meters, 'in'))
print(converter(length_in_meters, 'sj'))