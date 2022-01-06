import datetime
import time
def decorator_logger(function_to_decorate):
    def wrapp(*args, **kwargs):
        print(*args, **kwargs)
        start_time = datetime.datetime.now()
        result = function_to_decorate(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
        return result
    return wrapp
@decorator_logger
def lucky_ticket(*args, **kwargs):
    tickets = list(range(000000, 1000000, 1))
    counter = 0
    for x in range(len(tickets)):
        st = str(x)
        st = '0' * (6 - len(st)) + st
        if int(st[0]) + int(st[1]) + int(st[2]) == int(st[3]) + int(st[4]) + int(st[5]):
            counter += 1
    print('Cчастливых билетов:', counter)
@decorator_logger
def a1(*args, **kwargs):
    print(*args)
    print(**kwargs)



lucky_ticket(1, 2)
a1(159, 'abc')