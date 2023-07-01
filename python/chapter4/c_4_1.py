import math

import numpy as np

"""
```
def estimate(pi, delta=0.5, precision=0.9, gamma=0.9):
    S = []
    V = [0.0] * len(S)
    V_f = 0.0
    while True:
        D = 0.0
        for s in S:
            v = V[s]
            tmp = 0.0
            for a in pi(s):
                V[s] = a * 0 * (r + gamma * V[s_])
        D = max(D, abs(v - V[s]))
        if D < delta:
            break
```
"""


def translate_signal(dir_list: list):
    """
    ╬
    ╝╔╚╗
    ←→↑↓
    :param dir_list:
    :return:
    """
    if len(dir_list) == 0:
        return ''
    if len(dir_list) == 1:
        d = dir_list[0]
        if d == 0:
            return '←'
        if d == 1:
            return '↑'
        if d == 2:
            return '→'
        if d == 3:
            return '↓'
    if len(dir_list) == 2:
        dir_list.sort()
        if dir_list == [0, 1]:
            # return '╝'
            return '↖'
        if dir_list == [1, 2]:
            # return '╚'
            return '↗'
        if dir_list == [2, 3]:
            # return '╔'
            return '↘'
        if dir_list == [0, 3]:
            # return '╗'
            return '↙'

    if len(dir_list) == 4:
        return "┼"

    return ''


def init_S():
    return np.zeros(shape=(4, 4), dtype=float)


def init_max_idx():
    ret = []
    for _ in range(4):
        ret.append([None] * 4)
    return ret


def check_range(n, rang):
    return 0 <= n < rang


def cal_v_k(i, j, S, gamma=0.9, iter_time=0, k=0):
    if iter_time > k:
        return 0.0, []

    if (i == 0 and j == 0) or (i == 3 and j == 3):
        return 0.0, []

    i_dir = [0, -1, 0, 1]
    j_dir = [-1, 0, +1, 0]

    n, m = S.shape
    v = 0.0

    max_tmp = -math.inf
    max_idx = []

    for d in range(4):
        new_i = i + i_dir[d]
        new_j = j + j_dir[d]
        if not check_range(new_i, n) or not check_range(new_j, m):
            tmp, _ = cal_v_k(i, j, S, iter_time=iter_time + 1, k=k)
            tmp = 0.25 * (-1 + gamma * tmp)
        else:
            tmp, _ = cal_v_k(new_i, new_j, S, iter_time=iter_time + 1, k=k)
            tmp = 0.25 * (-1 + gamma * tmp)

        v += tmp

        if round(tmp, 1) > round(max_tmp, 1):
            max_tmp = tmp
            max_idx = [d]
            continue

        if round(tmp, 1) == round(max_tmp, 1):
            max_idx.append(d)
            continue

    return v, max_idx


def run(k):

    S = init_S()
    max_idx_matrix = init_max_idx()
    n, m = S.shape
    for i in range(n):
        for j in range(m):
            S[i][j], max_idx_matrix[i][j] = cal_v_k(i, j, S, k=k)

    S = S.round(1)
    # print(S)
    # print(max_idx_matrix)

    signal_matrix = init_max_idx()
    for i in range(n):
        for j in range(m):
            signal_matrix[i][j] = translate_signal(max_idx_matrix[i][j])

    for r in signal_matrix:
        print(r)


if __name__ == '__main__':
    print('=================')
    run(k=5)
    print('=================')
    run(k=6)
    print('=================')
