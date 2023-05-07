import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('./data/fifa_data.csv')

# histogram

bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa['Overall'], bins=bins, color='#abcdef')
plt.xlabel('Number of players')
plt.ylabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')

plt.show()
