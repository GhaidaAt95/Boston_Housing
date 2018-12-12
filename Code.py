import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import ShuffleSplit

data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)
print("Boston housing dataset has {} data points with {} variables each.".format(*data.shape))

minimum_price = np.amin(prices)

maximum_price = np.amax(prices)

mean_price = np.mean(prices)

median_price = np.median(prices)

std_price = np.std(prices)

print("Statistics for Boston housing dataset:\n")
print("Minimum price: ${}".format(minimum_price)) 
print("Maximum price: ${}".format(maximum_price))
print("Mean price: ${}".format(mean_price))
print("Median price ${}".format(median_price))
print("Standard deviation of prices: ${}".format(std_price))

plt.scatter(data['RM'],prices)
print(data['RM'].shape)
plt.plot(data['RM'],np.full(data['RM'].shape,mean_price))
plt.show()