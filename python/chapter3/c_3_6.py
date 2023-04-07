import math

import numpy as np


def init_S():
    return np.zeros(shape=(5, 5))


def init_max_idx():
    ret = []
    for _ in range(5):
        ret.append([None] * 5)
    return ret


def cal_v_pi_s(iter_time=0):
    pr = [0.25, 0.25, 0.25, 0.25]
    r = [0, 0, -1, -1]

    v_pi_s = 0.0
    for idx, p in enumerate(pr):
        if iter_time <= 10:
            v_pi_s += p * (r[idx] + cal_v_pi_s(iter_time + 1))

    return v_pi_s


def cal_v(i, j, S, iter_time=0, gamma=0.9, v_c=0.0):
    if iter_time >= 5:
        return 0.0, []
    i_dir = [0, -1, 0, 1]
    j_dir = [-1, 0, +1, 0]
    v = 0.0

    # State A
    if i == 0 and j == 1:
        r, _ = cal_v(4, 1, S, iter_time + 1, v_c)
        return gamma * r + 10 + v_c, [0, 1, 2, 3]

    # State B
    if i == 0 and j == 3:
        r, _ = cal_v(2, 3, S, iter_time + 1, v_c)
        return gamma * r + 5 + v_c, [0, 1, 2, 3]

    n, m = S.shape

    max_tmp = -math.inf
    max_idx = []
    for d in range(4):

        if i + i_dir[d] < 0 or i + i_dir[d] >= n or \
                j + j_dir[d] < 0 or j + j_dir[d] >= m:
            tmp_r, _ = cal_v(i, j, S, iter_time + 1, v_c)
            tmp = -1 + gamma * tmp_r
        else:
            tmp_r, _ = cal_v(i + i_dir[d], j + j_dir[d], S, iter_time + 1, v_c)
            tmp = gamma * tmp_r

        if round(tmp, 2) > round(max_tmp, 2):
            max_idx = [d]
            max_tmp = tmp
            continue

        if round(tmp, 2) == round(max_tmp, 2):
            max_idx.append(d)
            continue

    v += max_tmp

    return v + v_c, max_idx


def cal_v_tbl():
    S = init_S()
    max_idx_matrix = init_max_idx()
    n, m = S.shape
    for i in range(n):
        for j in range(m):
            S[i][j], max_idx_matrix[i][j] = cal_v(i, j, S)

    S = S.round(1)
    print(S)
    print(max_idx_matrix)


def fix_strategy(strategy='left', gamma=0.0, iter_time=0):
    if iter_time >= 10:
        return 0.0
    v = 0.0
    if strategy == 'left':
        v += 0 + gamma * practice_3_22(strategy, gamma, iter_time + 1)
    else:
        v += 2 + gamma * practice_3_22(strategy, gamma, iter_time + 1)

    return v


def practice_3_22(strategy='left', gamma=0.0, iter_time=0):
    if iter_time >= 10:
        return 0.0
    v = 0.0
    if strategy == 'left':
        v += 1 + gamma * fix_strategy(strategy, gamma, iter_time + 1)
    else:
        v += gamma * fix_strategy(strategy, gamma, iter_time + 1)

    return v


def print_result():
    print(f'gamma = {0}, strategy = left, revenue = {practice_3_22("left", 0, 0)}')
    print(f'gamma = {0}, strategy = right, revenue = {practice_3_22("right", 0, 0)}')
    print(f'gamma = {0.9}, strategy = left, revenue = {practice_3_22("left", 0.9, 0)}')
    print(f'gamma = {0.9}, strategy = right, revenue = {practice_3_22("right", 0.9, 0)}')
    print(f'gamma = {0.5}, strategy = left, revenue = {practice_3_22("left", 0.5, 0)}')
    print(f'gamma = {0.5}, strategy = right, revenue = {practice_3_22("right", 0.5, 0)}')


if __name__ == '__main__':

    print(cal_v_pi_s())
