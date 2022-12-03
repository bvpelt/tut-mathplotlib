import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Explicit and implicit interfaces - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#the-explicit-and-the-implicit-interfaces')

x = np.linspace(0, 2, 100)  # Sample data.
print('x: ', x)
sinval = []
for i in range(len(x)):
    sinval.append(4 + 4*math.sin(x[i]*math.pi))

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
#fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.plot(x, sinval, label='sinus')

ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.

ax.legend(loc="upper left");  # Add a legend.

plt.show()