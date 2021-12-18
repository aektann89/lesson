list_in = [(1, 'sm'), (2, 'ft'), (4, 'in'), (0.5, 'sm')]


def converter(measure_obj):
    convert_type = measure_obj[1]
    length_in_meters = measure_obj[0]
    result = 0
    if convert_type == 'sm':
        result = f'{(length_in_meters * 100)} сантиметров'
    elif convert_type == 'ft':
        result = f'{(length_in_meters * 3.281)} футов'
    elif convert_type == 'in':
        result = f'{(length_in_meters * 39.37)} дюймов'
    elif convert_type == 'sj':
        result = f'{(length_in_meters / 1.829)} саженей'
    else:
        result = 'Unknown'
    return result


result = map(converter, filter(lambda itm_in: True if itm_in[0] >= 1 else False, list_in))
for itm in result:
    print(itm)
