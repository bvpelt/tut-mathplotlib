import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Working with multiple Figures and Axes - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#working-with-multiple-figures-and-axes')


fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['lowleft'].set_title('lowleft')
axd['right'].set_title('right');
plt.show()