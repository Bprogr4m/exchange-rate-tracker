# Currency Exchange Rate Tracker

import numpy as np
import matplotlib.pyplot as plt

# Simulated Naira to USD exchange rates for a week
exchange_rates = np.array([1350, 1365, 1372, 1360, 1378, 1385, 1375])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Basic statistics
mean_rate = np.mean(exchange_rates)
max_rate = np.max(exchange_rates)
min_rate = np.min(exchange_rates)

print("Average Exchange Rate (NGN to USD):", mean_rate)
print("Maximum Exchange Rate:", max_rate)
print("Minimum Exchange Rate:", min_rate)

# Line plot
plt.figure(figsize=(10, 5))
plt.plot(days, exchange_rates, marker='o', linestyle='-', color='green')
plt.title('Simulated Weekly Naira to USD Exchange Rates')
plt.xlabel('Day of the Week')
plt.ylabel('Exchange Rate (NGN)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(7, 5))
plt.hist(exchange_rates, bins=5, color='orange', edgecolor='black')
plt.title('Distribution of Exchange Rates')
plt.xlabel('Exchange Rate Range (NGN)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
