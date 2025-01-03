# -*- coding: utf-8 -*-
"""lab3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18AC3Ex1gyxLcSws3RwXAudxonRBWb3pr
"""

import matplotlib.pyplot as plt

n=[128,256,512,1024,2048,4096]
Traditional=[0.008,0.074,0.477,5.734,109.054,1962.552]
Strassen=[0.011,0.048,0.331,2.265,15.85,94.159]

plt.plot(n, Traditional, marker='o', label='Traditional Matrix Multiplication')
plt.plot(n, Strassen, marker='o', label='Strassen\'s Matrix Multiplication')


plt.xlabel('Matrix Size (n*n)')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Performance Comparison')
plt.legend()
plt.grid(True)

plt.show()