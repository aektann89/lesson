while True:
    numbers = input("Введите число:\n")

    if numbers == "exit":
        break
    for num in range(2, int(numbers)):
        if all(num % x != 0 for x in range(2, num)):
            print(num)
    print("Введите exit если хотите закрыть программу")