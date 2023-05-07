import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 4, 5, 6]

# adding properties to the graph
plt.plot(x, y, label='2x', linestyle='--', color='g', linewidth=2, marker='.', markersize=10, markeredgecolor='r') # given two arrays of x and y values

# adding labels

plt.title('My first graph!', fontdict={'fontname': 'Comic Sans Ms', 'fontsize': 20})
plt.xlabel('X axis')
plt.ylabel('Y axis')

# changing the ticks

plt.xticks([0, 1, 2, 3])
plt.yticks([0, 2, 4, 6, 8, 10])

plt.legend() # adding a legend

plt.show() # showing the graph
