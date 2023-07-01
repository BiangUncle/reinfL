import numpy as np
import matplotlib.pyplot as plt

N_STATES = 1000

bases = []
order = 20
for i in range(0, order + 1):
    # bases.append(lambda s, i=i: np.cos(i * np.pi * s))
    bases.append(lambda s, i=i: pow(s, i))


state = 500
state /= float(N_STATES)
# get the feature vector
feature = np.asarray([func(state) for func in bases])
print(feature)

state = 250
state /= float(N_STATES)
# get the feature vector
feature_2 = np.asarray([func(state) for func in bases])
print(feature_2)

state = 750
state /= float(N_STATES)
# get the feature vector
feature_3 = np.asarray([func(state) for func in bases])
print(feature_3)


plt.plot([i for i in range(0, order + 1)], feature)
plt.plot([i for i in range(0, order + 1)], feature_2)
plt.plot([i for i in range(0, order + 1)], feature_3)
plt.show()
