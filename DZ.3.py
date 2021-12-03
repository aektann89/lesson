while True:
    print("Введите exit что бы завершить работу с программой")
    num1 = (input["Введите число"])
    action = input("Введите оператор: (+,-,*,/)")
    num2 = (input["num2="])
    if action and num1 and num2 == 'exit':
        break



    # if action in ('+', '-', '*', '/'):
    #
    #     if action == "+":
    #         print(num1+num2)
    #     elif action == '-':
    #         print(float(num1)-float(num2))
    #     elif action == '*':
    #         print(num1*num2)
    #     elif action == '/':
    #         print(float(num1)/float(num2))
    #
    #
    # else:
    #     print("Указанный оператор не существует")