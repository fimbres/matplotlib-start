import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4.5, 0.5)
plt.plot(x[:5], x[:5]**2, 'b', label='x^2')
plt.plot(x[4:], x[4:]**2, 'r--')

plt.savefig('./saved_graphs/first_graph.png', dpi=300)

plt.show()
