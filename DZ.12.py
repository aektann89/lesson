import datetime
import time

def lucky_ticket():
    tickets = list(range(000000, 1000000, 1))
    counter = 0
    for x in range(len(tickets)):
        st = str(x)
        st = '0' * (6 - len(st)) + st
        if int(st[0]) + int(st[1]) + int(st[2]) == int(st[3]) + int(st[4]) + int(st[5]):
            counter += 1
    print('Cчастливых билетов:', counter)

def calc_time(func_in, *args, **kwargs):
    start_time = datetime.datetime.now()

    val_in_func = func_in(*args, **kwargs)

    end_time = datetime.datetime.now()
    print(end_time - start_time)
    return val_in_func
val1 = calc_time(lucky_ticket)
