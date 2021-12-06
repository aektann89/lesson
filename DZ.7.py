while True:
    list = input("Введите строку: ")
    src = input("Введите слово которое нужно найти и заменить: ")
    if src not in list:
        print('Такого слова нет в вашей строке')
        continue
    elif src in list:
        rpt = input("Введите слово-замену: ")
    print("Замена произведена:")
    print(list.replace(src, rpt))
    print('Количество замен:', list.count(src))


