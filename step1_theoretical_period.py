# Liv Moore and Soham Dave
# There is one primary limitation with this model that could affect its 
# ecological validity (e.g. how well it translates to the real world). 
# We assumed that air resistance does not slow down the pendulum. Air 
# resistance continually acting on the pendulum is what causes it to 
# eventually come to a stop and decreases every consecutive period as time 
# elapses. Our model also assumes that the bar of the pendulum is massless, 
# but in reality, the mass of the bar would slow down the pendulum’s 
# acceleration. Overall, it is incorrect to assume that the pendulum’s motion 
# is perfect and smooth, and as a result, the model does not accurately 
# calculate the average period over time.

import matplotlib.pyplot as plt
import math

def calculate_periods():
    # calculates the theoretical periods of the pendulum at the various lengths
    # used.
    # takes no arguments.
    # returns an array of the periods
    lengthData = [0.018, 0.0245, 0.0315, 0.039, 0.0485]
    period = [0] * len(lengthData)
    for i in range(len(lengthData)):
        period[i] = round(2 * 3.14159 * math.sqrt(lengthData[i]/9.81),2)
    return period
   
def plot_periods():
    # plots the theoretical periods found in calculate_periods as a function
    # of the lengths of pendulums.
    # takes no arguments.
    # void function.
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.title('How Pendulum Length Affects Period')
    plt.plot(lengthData, calculate_periods())
    plt.show()
    
print(calculate_periods())
plot_periods()