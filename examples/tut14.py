import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

print('Plotting dates and strings - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#plotting-dates-and-strings')


#fig, axs = plt.subplots(2, 1, figsize=(5, 2.7), layout='constrained')
fig, axs = plt.subplots(2, 1,  layout='constrained')
dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                  np.timedelta64(1, 'h'))
data = np.cumsum(np.random.randn(len(dates)))
axs[0].plot(dates, data)
cdf = mpl.dates.ConciseDateFormatter(axs[0].xaxis.get_major_locator())
axs[0].xaxis.set_major_formatter(cdf);

categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

axs[1].bar(categories, np.random.rand(len(categories)));

plt.show()