import random
import bisect
import numpy as np
from base import *
import matplotlib.pyplot as plt

# 梯度赌博机


def init_H(action_num):
    return [0.0] * action_num


def choose_pr(probability: list):
    acc_list = []
    acc = 0.0
    for p in probability:
        acc += p
        acc_list.append(acc)

    r = random.random()
    return bisect.bisect_left(acc_list, r)


def cal_pr(H):
    return np.exp(H) / np.sum(np.exp(H))


def cal_H(H, a, R, R_mean, pr, alpha):
    step = alpha * (R - R_mean)
    for i in range(len(H)):
        if i == a:
            H[i] = H[i] + step * (1 - pr[i])
        else:
            H[i] = H[i] - step * pr[i]

    return H


def test_pr():
    print([cal_pr([0.1, 0.2, 0.3, 0.4], 0),
           cal_pr([0.1, 0.2, 0.3, 0.4], 1),
           cal_pr([0.1, 0.2, 0.3, 0.4], 2),
           cal_pr([0.1, 0.2, 0.3, 0.4], 3),
           ])
    print([cal_pr([0.25, 0.25, 0.25, 0.25], 0),
           cal_pr([0.25, 0.25, 0.25, 0.25], 1),
           cal_pr([0.25, 0.25, 0.25, 0.25], 2),
           cal_pr([0.25, 0.25, 0.25, 0.25], 3),
           ])


def run(alpha: float, times: int, action_num: int):
    i = 1
    Q, N = init(action_num)
    H = init_H(action_num)

    selected_time = [0] * action_num
    selected_revenue = [[] for _ in range(action_num)]

    total_R = 0.0
    y = []
    x = []

    while True:
        pr = cal_pr(H)
        a = choose_pr(pr)
        R = bandit(Q[a])
        selected_time[a] += 1
        selected_revenue[a].append(R)

        total_R += R
        y.append(total_R / i)
        x.append(i)

        N[a] = N[a] + 1
        Q[a] = np.mean(selected_revenue[a])

        for j in range(len(Q)):
            Q[j] += add_random_incr()

        H = cal_H(H, a, R, total_R / i, pr, alpha)

        i += 1
        if i >= times:
            break

    return x, y


if __name__ == '__main__':
    x, y = run(0.1, 1000, 10)
    plt.plot(x, y)
    plt.show()

