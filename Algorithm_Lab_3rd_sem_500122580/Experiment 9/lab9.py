# -*- coding: utf-8 -*-
"""lab9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FdUmYxinx4euXbgN5Cqysl7PxtAfoHQI
"""

import matplotlib.pyplot as plt

# Weights and corresponding times
weights= [100, 200, 400]
backtracking_times = [0.0002, 0.0004, 0.0006]
branch_and_bound_times = [0.0006, 0.0009, 0.0009]
dp_times = [0.0027, 0.0057,0.0126 ]

# Plotting each algorithm's times
plt.figure(figsize=(10, 6))
plt.plot(weights, backtracking_times, label='Backtracking', marker='o', color='r')
plt.plot(weights, branch_and_bound_times, label='Branch & Bound', marker='s', color='g')
plt.plot(weights, dp_times, label='Dynamic Programming', marker='^', color='b')

# Adding labels and title
plt.xlabel('Weights')
plt.ylabel('Execution Time (ms)')
plt.title('0/1 Knapsack Problem: Performance Comparison')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()