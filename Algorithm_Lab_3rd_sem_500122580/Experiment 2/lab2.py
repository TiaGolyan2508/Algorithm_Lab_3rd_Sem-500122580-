# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H8RhZasA6emO6J6k9KLRglf7M4YF1-58
"""

import matplotlib.pyplot as plt

n=[10000,20000,30000,40000,50000,60000]
Merge_Sort=[0.003,0.007,0.01,0.022,0.03,0.039]
Quick_Sort=[0.002,0.007,0.008,0.013,0.015,0.019]

plt.plot(n, Merge_Sort, marker='o', label='Merge Sort Performance')
plt.plot(n, Quick_Sort, marker='o', label='Quick Sort Performance')


plt.xlabel('Array Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Performance Comparison')
plt.legend()
plt.grid(True)

plt.show()