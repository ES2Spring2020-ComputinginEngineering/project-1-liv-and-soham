# Liv Moore and Soham Dave

import math
  
# CUSTOM FUNCTIONS:
      
def plot_position_time(time, position):
    # plots the simulated angular position of a pendulum of a certain length
    # as a function of time.
    # takes arrays of time and position of the pendulum.
    # void function.
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Position (radians)")
    plt.title("Angular Position vs. Time")
    plt.plot(time, position)
    plt.show()
    
def plot_velocity_time(time, velocity):
    # plots the simulated angular velocity of a pendulum of a certain length 
    # as a function of time.
    # takes arrays of time and velocity of the pendulum.
    # void function.
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Velocity (radians per second)")
    plt.title("Angular Velocity vs. Time")
    plt.plot(time, velocity)
    plt.show()
    
def plot_acceleration_time(time, acceleration):
    # plots the simulated angular acceleration of a pendulum of a certain 
    # length as a function of time.
    # takes arrays of time and acceleration of the pendulum.
    # void function.
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Acceleration (radians per second squared)")
    plt.title("Angular Acceleration vs. Time")
    plt.plot(time, acceleration)
    plt.show()
    
def find_period(time, angles):
    # finds the period of a simulated pendulum of a certain length.
    # takes arrays of time and angles of simulated pendulum
    # returns a float, the period of the pendulum.
    plt.plot(time, angles)
    peaksseries = find_peaks(angles, distance=50)[0]
    differencetime = int(peaksseries[3] - peaksseries[2])
    period = differencetime
    return period

def plot_periods():
    # plots the periods of simulated pendulums found by calculations as a
    # function of the lengths of the pendulums.
    # takes no arguments. void function.
    lengths = [18,24.5,31.5,39,48.5]
    periods = [1.1762,1.371,1.5535,1.7276,1.9257]
    plt.xlabel("Length (cm)")
    plt.ylabel("Period (seconds)")
    plt.title("Period vs. Length of Pendulum")
    plt.plot(lengths, periods)
    plt.show()

# MAIN SCRIPT

length = 0.485
pos = (math.pi)/3
a = 0
v = 0
dt = 1/10000
currenttime = 0
timearray = []
varray = []
aarray = []
posarray = []
while currenttime < 10:
    pos = pos + v*dt
    posarray.append(pos)
    v = v + a*dt
    varray.append(v)
    a = -(9.81*math.sin(pos))/length
    aarray.append(a)
    currenttime += dt
    timearray.append(currenttime)
    
plot_position_time(timearray, posarray)
plot_velocity_time(timearray, varray)
plot_acceleration_time(timearray, aarray)