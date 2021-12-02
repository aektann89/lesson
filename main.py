while True:
    def inp_ut(operator):
        while True:
            try:
                text = '{} {} {} '.format("Введите, пожалуйста", operator, '>>>')
                sign_ = str(input(text))
                return sign_
            except ValueError:
                print("Не правильный оператор")


    sign_ = inp_ut('оператор: (+,-,*,/)')


    def inp_ut(nums):
        while True:
            try:
                text = '{} {} {} '.format("Введите, пожалуйста,", nums, '>>>')
                num_1 = float(input(text))
                return num_1
            except ValueError:
                print("Вы ввели не число, попробуйте еще раз...")


    num1 = inp_ut('Первое число')
    num2 = inp_ut('Второе число')
    if sign_ in ('+', '-', '*', '/'):
        if sign_ == '+':
            print(num1 + num2)
        if sign_ == '-':
            print(num1 - num2)
        if sign_ == '*':
            print(int(num1) * int(num2))
        if sign_ == '/':
            print(num1 / num2)
