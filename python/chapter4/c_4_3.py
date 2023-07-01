import math
import matplotlib.pyplot as plt
from base import *
import seaborn as sns


def factorial(n):
    v = 1
    for i in range(2, n + 1):
        v *= i

    return v


def poisson_pr(phi, n):
    return ((phi ** n) / factorial(n)) * math.e ** (-phi)


def get_poisson_result(phi):
    r = random()
    i = 0
    acc = 0.0
    while True:
        pr = poisson_pr(phi, i)
        acc += pr
        if r <= acc:
            return i
        i += 1


def draw_poisson_pr_pics():
    x = []
    y = []
    acc = 0.0
    acc_list = []
    for i in range(11):
        x.append(i)
        pr = poisson_pr(0.9, i)
        y.append(pr)
        acc += pr
        acc_list.append(acc)

    plt.plot(x, y)
    plt.plot(x, acc_list)
    plt.show()


if __name__ == '__main__':
    data = []
    for _ in range(1000):
        data.append(get_poisson_result(3))

    sns.kdeplot(data)
    plt.show()