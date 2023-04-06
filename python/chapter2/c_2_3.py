import random
import matplotlib.pyplot as plt
import numpy as np

r = random.random()

plt.violinplot(dataset=np.random.normal(1, 1, 1000))
plt.show()
