import numpy as np


class RetrieveM:
    """
    :math:`q_\pi()`
    """
    high = 1
    low = 2
    S = [high, low]

    search = 1
    wait = 2
    recharge = 3

    action = {
        high: [search, wait],
        low: [search, wait, recharge],
    }

    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        np.exp()


