from c_2_4 import *
import math


def cal_new_Q(history_revenue: list, Q_1, alpha, O):
    n = len(history_revenue)
    Q_n1 = ((1 - alpha) ** n) * Q_1
    # if n == 100:
    #     print('stop here')
    for i in range(1, n + 1):
        O_n = cal_o(alpha, O[i - 1])
        beta = alpha / O_n
        Q_n1 += beta * history_revenue[i - 1]
        if i == n and len(O) < len(history_revenue) + 1:
            O.append(O_n)
    return Q_n1


def cal_o(alpha, o_n_1):
    return o_n_1 + alpha * (1 - o_n_1)


def run(epsilon: float, times: int, action_num: int, alpha):
    i = 1
    Q, N = init(action_num)
    Q_1 = [math.inf] * action_num
    O_n_1 = [[0.0] for _ in range(action_num)]
    Q_record = [[] for _ in range(action_num)]

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
            Q[a] = cal_new_Q(selected_revenue[a], 1.0, alpha, O_n_1[a])
            Q_1[a] = Q[a]
        else:
            Q[a] = cal_new_Q(selected_revenue[a], Q_1[a], alpha, O_n_1[a])
        Q_record[a].append(Q[a])

        for j in range(len(Q)):
            Q[j] += add_random_incr()

        i += 1
        if i >= times:
            break

    for i in range(len(Q_record)):
        plt.plot(np.arange(len(Q_record[i])), Q_record[i])
    plt.show()

    return x, y


def test_beta():
    o = [0.0]
    x = [0]
    alpha = 0.1
    for i in range(1, 1001):
        new_o = o[i - 1] + alpha * (1 - o[i - 1])
        o.append(new_o)
        x.append(i)

    plt.plot(x, o)
    plt.show()


if __name__ == '__main__':
    x, y = run(0.1, 1000, 10, 0.1)
    plt.plot(x, y)
    plt.show()

