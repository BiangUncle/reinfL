import numpy as np
import math


def softmax(num):
    x_exp = np.exp(num)
    # 如果是列向量，则axis=0
    x_sum = np.sum(x_exp, axis=0, keepdims=True)
    s = x_exp / x_sum
    return s


def sigmoid(num):
    return 1 / (1 + math.exp(-num))

