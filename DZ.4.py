for x in list(range(000000, 1000000, 1)):
    a = int(x)
    sum_main = 0
    sum_second = 0
    for x in range(6):
        if x < 3:
            sum_main += a // 10 ** x % 10
        else:
            sum_second += a // 10 ** x % 10
    if sum_second == sum_main:
        print('lucky')
    else:
        print("unlucky")
