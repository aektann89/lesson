while True:
    ford = ['mondeo', 'focus', 'kuga']
    fiat = ['tipo', 'panda', '500']
    renault = ['clio', 'megan', 'duster']
    print('Введите модель автомобиля\nВведите exit если хотите выйти\n')
    action = input()
    if action == 'exit':
        break

    if action in ford:
        print("ford")
    elif action in fiat:
        print('fiat')
    elif action in renault:
        print("renault")
    else:
        print("Введенная модель автомобиля не соответствует ни одной из известных программе марок автомобилей")
