import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

x = np.array([3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.3])
y = np.array([-4.4256712, -4.66147, -4.7979864, -4.8645042, -4.8773847, -4.8487437, -4.7852634, -4.6936947, -4.5831167])

fig, ax = plt.subplots(figsize=(8, 6))
# ax.scatter(x, y, marker='s', s=50, c='C0', edgecolors=(0.122, 0.467, 0.706, 0.6), linewidths=3)
ax.plot(x, y, c='C0', marker='s', ms=7, mec=(0.122, 0.467, 0.706, 0.6), mew=3, lw=2)
# ax.axhline(y=-14.23905528, ls='--', c='k', lw=2, alpha = 0.5)
ax.set_xlabel('Lattice parameter (Å)')
ax.set_ylabel('Energy (eV)')

mpt.minor(ax)
mpt.savepdf('fccSi')
plt.show()