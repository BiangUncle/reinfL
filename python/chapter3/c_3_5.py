import numpy as np


def init_S():
    return np.zeros(shape=(5, 5))


def cal_v_pi_s(iter_time=0):
    pr = [0.25, 0.25, 0.25, 0.25]
    r = [0, 0, -1, -1]

    v_pi_s = 0.0
    # for idx, p in enumerate(pr):
    #     v_pi_s += p * r[idx]
    #
    # print(v_pi_s)
    for idx, p in enumerate(pr):
        if iter_time <= 10:
            v_pi_s += p * (r[idx] + cal_v_pi_s(iter_time + 1))

    return v_pi_s


def cal_v(i, j, S, iter_time=0, gamma=0.9, v_c=0.0):
    if iter_time >= 6:
        return 0.0
    i_dir = [0, -1, 0, 1]
    j_dir = [-1, 0, +1, 0]
    v = 0.0

    # State A
    if i == 0 and j == 1:
        v += 10 + gamma * cal_v(4, 1, S, iter_time + 1, v_c)
        return v + v_c

    # State B
    if i == 0 and j == 3:
        v += 5 + gamma * cal_v(2, 3, S, iter_time + 1, v_c)
        return v + v_c

    n, m = S.shape

    for d in range(4):

        if i + i_dir[d] < 0 or i + i_dir[d] >= n or \
                j + j_dir[d] < 0 or j + j_dir[d] >= m:
            v += 0.25 * (-1 + gamma * cal_v(i, j, S, iter_time + 1, v_c))
        else:
            v += 0.25 * gamma * cal_v(i + i_dir[d], j + j_dir[d], S, iter_time + 1, v_c)

    return v + v_c


def cal_v_tbl():
    S = init_S()
    n, m = S.shape
    for i in range(n):
        for j in range(m):
            S[i][j] = cal_v(i, j, S)

    S = S.round(1)
    print(S)


if __name__ == '__main__':

    # print(cal_v_pi_s())
    cal_v_tbl()
