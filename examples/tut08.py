import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Linewidth, linestyles and markersizes - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#linewidths-linestyles-and-markersizes')

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets

#fig, ax = plt.subplots(figsize=(5, 2.7))
fig, (ax, ax2) = plt.subplots(1,2)
ax2.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k', label='data1');
ax2.legend()

#fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, data1, 'o', label='data1')
ax.plot(data1, data2, 'd', label='data2')
ax.plot(data1, data3, 'v', label='data3')
ax.plot(data1, data4, 's', label='data4')
ax.legend();

plt.show()