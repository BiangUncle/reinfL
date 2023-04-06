import numpy as np
import random


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
