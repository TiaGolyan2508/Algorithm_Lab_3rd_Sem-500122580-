# -*- coding: utf-8 -*-
"""lab10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zb4dJhKLSLo457n-VKbI-WSDAHHUoAoB
"""

import matplotlib.pyplot as plt

Inputs= [1, 2, 3, 4, 5]
Rabin = [0.003, 0.002, 0.003,0.006,0.005]
Knuth = [0.001, 0.002, 0.001,0.001,0.0]
Naive = [0.002, 0.001,0.001, 0.006,0.004]

# Plotting each algorithm's times
plt.figure(figsize=(10, 6))
plt.plot(Inputs, Rabin, label='Rabin-Karp', marker='o', color='r')
plt.plot(Inputs, Knuth, label='Knuth-Morris-Pratt', marker='s', color='g')
plt.plot(Inputs, Naive, label='Naive String Matching', marker='^', color='b')

# Adding labels and title
plt.xlabel('Inputs')
plt.ylabel('Execution Time (ms)')
plt.title('Comparison of different String Matching Algorithms')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()