import random
import numpy as np
from base import *
import matplotlib.pyplot as plt


def select_action(Q: list, N_t: list, t, c=1):

    result = np.array(Q) + c * np.sqrt(np.log(t / np.array(N_t)))

    # test_result = [0.0] * len(Q)
    # for i in range(len(Q)):
    #     test_result[i] = Q[i] + c * np.sqrt(np.log(t) / N_t[i])

    return np.argmax(result)


def run(epsilon: float, times: int, action_num: int):
    i = 1
    Q, N = init(action_num)

    selected_time = [0] * action_num
    selected_revenue = [[] for _ in range(action_num)]

    total_R = 0.0
    y = []
    x = []

    while True:
        a = select_action(Q, N, i)
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

        i += 1
        if i >= times:
            break

    return x, y


if __name__ == '__main__':
    x, y = run(0.1, 1000, 10)
    plt.plot(x, y)
    plt.show()