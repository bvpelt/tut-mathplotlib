import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print('Types of inputs to plotting functions - https://matplotlib.org/stable/tutorials/introductory/quick_start.html#types-of-inputs-to-plotting-functions')

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

print ('before')
print('a: ', data['a'])
print('c: ', data['c'])
print('d: ', data['d'])

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

print ('after')
print('a: ', data['a'])
print('b: ', data['b'])
print('c: ', data['c'])
print('d: ', data['d'])

#fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
#fig, ax = plt.subplots( layout='constrained')
fig, ax = plt.subplots( )
scatter = ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b');

legend1 = ax.legend(*scatter.legend_elements(), loc="upper left")
ax.add_artist(legend1)

plt.show()