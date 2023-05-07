import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values)
bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')

plt.show()
