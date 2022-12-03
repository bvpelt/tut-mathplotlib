import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Tick locators and formatters - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#tick-locators-and-formatters')


data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
xdata = np.arange(len(data1))  # make an ordinal for this

fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks');

plt.show()