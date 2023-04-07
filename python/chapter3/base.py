import numpy as np
import bisect


def choose_pr(probability: list):
    acc_list = []
    acc = 0.0
    for p in probability:
        acc += p
        acc_list.append(acc)

    r = np.random.random(1)[0]
    return bisect.bisect_left(acc_list, r)
