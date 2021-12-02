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