import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Making a helper functions - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#making-a-helper-functions')

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'});

plt.show()