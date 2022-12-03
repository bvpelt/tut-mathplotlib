import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Annotations - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#axes-labels-and-text')
mu, sigma = 125, 25
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
#ax.text(60, .025, r'$\mu=115,\ \sigma=15$')
string = '$\mu=%d,\ \sigma=%d$' %(mu, sigma)
ax.text(60, .025, string)
#ax.axis([55, 175, 0, 0.03])
minx = mu - 4*sigma
maxx = mu + 4*sigma
miny = 0
maxy = 0.030
ax.axis([minx, maxx, miny, maxy])
ax.grid(True);

plt.show()