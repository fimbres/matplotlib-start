import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('./data/fifa_data.csv')

# foot preference

labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbcc']
left = fifa.loc[fifa['Preferred Foot'] == "Left"].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == "Right"].count()[0]

plt.pie([left, right], labels = labels, colors = colors, autopct='%.3f %%')
plt.title('Foot Preference of FIFA Players')

plt.show()

# weights

fifa['Weight'] = [int(x.strip('lbs')) if type(x) == str else x for x in fifa['Weight']]

light = fifa.loc[fifa['Weight'] < 125].count()[0]
medium = fifa.loc[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
heavy = fifa.loc[fifa['Weight'] >= 200].count()[0]

labels2 = ['Light', 'Medium', 'Heavy']
colors2 = ['#abcdef', '#aabbcc', '#abcabc']

plt.pie([light, medium, heavy], labels = labels2, colors = colors2, autopct='%.3f %%', pctdistance=0.7, explode=(0, .2, .3))
plt.title('Weight distribution of FIFA Players (in lbs)')

plt.show()
