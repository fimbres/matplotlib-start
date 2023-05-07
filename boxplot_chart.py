import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('./data/fifa_data.csv')

fifa['Club Count'] = 0

clubs = fifa.groupby(['Club']).count()
print(clubs)

plt.boxplot(clubs)

plt.show()