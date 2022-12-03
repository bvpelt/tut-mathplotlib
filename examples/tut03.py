import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

print('Simple example - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#a-simple-example')

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], label='Data');  # Plot some data on the axes.

ax.set_title('Figure title')
ax.set_xlabel('X - values')
ax.set_ylabel('Y - values')
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.legend();

plt.show()