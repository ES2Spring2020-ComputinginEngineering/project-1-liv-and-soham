# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:19:26 2020

@author: moore
"""

import matplotlib.pyplot as plt
import math
lengthData = [0.018, 0.0245, 0.0315, 0.039, 0.0485]

def calculatePeriod(lengthData):
    period = [0] * len(lengthData)
    for i in range(len(lengthData)):
        period[i] = round(2 * 3.14159 * math.sqrt(lengthData[i]/9.81),2)
    return period
print(calculatePeriod(lengthData))
   

plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.title('How Pendulum Length Affects Period')
plt.plot(lengthData, calculatePeriod(lengthData))
plt.show()