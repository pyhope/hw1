import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

x = np.arange(200, 800, 100)
y = np.array([-14.30681123, -14.25697165, -14.2237071, -14.22392388, -14.23116785, -14.23656275])

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, marker='s', markersize=10, c='C0', markeredgecolor=(0.122, 0.467, 0.706, 0.6), markeredgewidth=2)
plt.show()