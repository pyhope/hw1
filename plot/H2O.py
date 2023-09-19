import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

x = np.arange(200, 1100, 100)
y = np.array([-14.30681123, -14.25697165, -14.2237071, -14.22392388, -14.23116785, -14.23656275, -14.23863381, -14.23896373, -14.23905528])

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x, y, marker='s', s=50, c='C0', edgecolors=(0.122, 0.467, 0.706, 0.6), linewidths=3)
ax.axhline(y=-14.23905528, ls='--', c='k', lw=2, alpha = 0.5)
ax.set_xlabel('ENCUT (eV)')
ax.set_ylabel('Energy (eV)')

mpt.minor(ax)
mpt.savepdf('H2O')