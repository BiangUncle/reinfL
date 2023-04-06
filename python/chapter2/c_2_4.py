import random
import matplotlib.pyplot as plt
import numpy as np


def add_random_incr():
    return np.random.normal(0, 0.01, 1)[0]


def init(action_num: int):
    Q = [0.0] * action_num
    N = [0.0] * action_num

    return Q, N


def select_action(Q: list, epsilon: float):

    randFloat = random.random()
    if randFloat < epsilon:
        action = random.randint(0, len(Q) - 1)
        return action

    action = np.argmax(Q)

    return action


def bandit(q_mean) -> float:
    return np.random.normal(q_mean, 1, 1)[0]


def run(epsilon: float, times: int, action_num: int):
    i = 1
    Q, N = init(action_num)

    selected_time = [0] * action_num
    selected_revenue = [[] for _ in range(action_num)]

    total_R = 0.0
    y = []
    x = []

    best_action_rate = []
    best_time = 0

    while True:

        best_a = np.argmax(Q)
        a = select_action(Q, epsilon)

        if a == best_a:
            best_time += 1
        best_action_rate.append(best_time / i)

        R = bandit(Q[a])
        selected_time[a] += 1
        selected_revenue[a].append(R)

        total_R += R
        y.append(total_R / i)
        x.append(i)

        N[a] = N[a] + 1
        Q[a] = Q[a] + (1 / N[a]) * (R-Q[a])

        for j in range(len(Q)):
            Q[j] += add_random_incr()

        i += 1
        if i > times:
            break

    # plt.plot(x, best_action_rate)
    # plt.show()

    # plt.violinplot(selected_revenue, showextrema=False, showmeans=True)
    # plt.title(f'epsilon = {epsilon}')
    # plt.show()

    return x, y
    # print(selected_time)


def draw_multi_pics():
    x1, y1 = run(0.01, 1000, 10)
    x2, y2 = run(0.1, 1000, 10)
    x3, y3 = run(0, 1000, 10)

    plt.plot(x1, y1, label='0.01')
    plt.plot(x2, y2, label='0.1')
    plt.plot(x3, y3, label='0')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # draw_multi_pics()
    x, y = run(0.1, 1000, 10)
    plt.plot(x, y)
    plt.show()
