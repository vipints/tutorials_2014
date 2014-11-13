import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)

plt.plot(x, y)       # line plot
plt.plot(x, y, 'o')  # dot plot 

plt.show()
