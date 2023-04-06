import math

import matplotlib.pyplot as plt

from c_2_4 import *


def cal_new_Q(history_revenue: list, Q_1, alpha):
    n = len(history_revenue)
    Q_n1 = ((1 - alpha) ** n) * Q_1
    # if n == 100:
    #     print('stop here')
    for i in range(1, n + 1):
        Q_n1 += alpha * ((1 - alpha) ** (n - i)) * history_revenue[i - 1]
    return Q_n1


def run(epsilon: float, times: int, action_num: int, alpha):
    i = 1
    Q, N = init(action_num)
    Q_1 = [math.inf] * action_num

    selected_time = [0] * action_num
    selected_revenue = [[] for _ in range(action_num)]

    total_R = 0.0
    y = []
    x = []

    while True:
        a = select_action(Q, epsilon)
        R = bandit(Q[a])
        selected_time[a] += 1
        selected_revenue[a].append(R)

        total_R += R
        y.append(total_R / i)
        x.append(i)

        N[a] = N[a] + 1
        if Q_1[a] == math.inf:
            Q[a] = cal_new_Q(selected_revenue[a], 1.0, alpha)
            Q_1[a] = Q[a]
        else:
            Q[a] = cal_new_Q(selected_revenue[a], Q_1[a], alpha)

        for j in range(len(Q)):
            Q[j] += add_random_incr()

        i += 1
        if i >= times:
            break

    return x, y


if __name__ == '__main__':
    x, y = run(0.1, 5000, 10, 0.1)
    plt.plot(x, y)
    plt.show()

