import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv('./data/gas_prices.csv')

plt.title('Gas Prices Over Time (USD)')

plt.plot(gas['Year'], gas['USA'], 'b.-', label='USA')
plt.plot(gas['Year'], gas['Canada'], 'g.-', label='Canada')
plt.plot(gas['Year'], gas['South Korea'], 'y.-', label='South Korea')
plt.plot(gas['Year'], gas['Australia'], 'r.-', label='Australia')

plt.xticks(gas['Year'][::3])

plt.xlabel('Year')
plt.ylabel('Price (USD)')

plt.legend()

plt.savefig('./saved_graphs/gas_graph.png')

plt.show()
