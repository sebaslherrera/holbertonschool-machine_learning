#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

apples = fruit[0][:]
bananas = fruit[1][:]
oranges = fruit[2][:]
peaches = fruit[3][:]

x = ['Farrah', 'Fred', 'Felicia']

# your code here
plt.bar(x, apples, color='red', width=0.5)
plt.bar(x, bananas, bottom=apples, color='yellow', width=0.5)
plt.bar(x, oranges, bottom=apples+bananas, color='#ff8000', width=0.5)
plt.bar(x, peaches, bottom=apples+bananas+oranges, color='#ffe5b4', width=0.5)
plt.title("Number of Fruit per Person")
plt.ylabel("Quantity of Fruit")
plt.legend(["apples", "bananas", "oranges", "peaches"])
plt.ylim(0, 80)

plt.show()
