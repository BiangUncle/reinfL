import time


def cal_cost_time(func):

    def wrapper(*args):
        local_time = time.time()
        func(*args)
        print('current Function [%s] run time is %.2f' % (func.__name__, time.time() - local_time))

    return wrapper
