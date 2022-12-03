import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Styling Artists - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#styling-artists')

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--', label='data1')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2, label='data2')
l.set_linestyle(':');
ax.plot(x, np.cumsum(data3), color='green', linewidth=2, linestyle='dashdot', label='data3')
ax.plot(x, np.cumsum(data4), color='red', linewidth=1, linestyle='dotted', label='data4')

ax.legend(loc="upper left")
plt.show()