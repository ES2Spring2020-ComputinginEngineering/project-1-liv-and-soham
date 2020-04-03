# Liv Moore and Soham Dave


import os
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt
from scipy.signal import find_peaks

path = "C:/users/moore/mu_code/data_capture"
os.chdir(path)

filename = "length 18.csv"

array = np.loadtxt(filename, delimiter=',', dtype=str)
newarray = array.astype('float64')


def find_theta(x, y):
    # finds the angle of the pendulum throughout its motion using x and y
    # accelerations.
    # takes x and y, which are arrays of the x and y accelerations recorded
    # by the microbit accelerometer.
    # returns an array of angles in degrees
    degreesseries = []
    for i in range(len(x)):
        radians = numpy.arctan(y[i]/x[i])
        degrees = 180*radians/numpy.pi
        degreesseries.append(degrees)
        cleanangles = sp.signal.medfilt(degreesseries)
    return cleanangles
    
def find_period(time, x, y):
    # finds the period of the pendulum, or how long it takes to complete one 
    # cycle of movement (e.g. from one end back to the same end).
    # takes time, x acceleration, and y acceleration arrays recorded by the 
    # microbit and microbit accelerometer.
    # returns a float, the period of the pendulum
    degreesseries = []
    for i in range(len(x)):
        radians = numpy.arctan(y[i]/x[i])
        degrees = 180*radians/numpy.pi
        degreesseries.append(degrees)
        cleanangles = sp.signal.medfilt(degreesseries)
    plt.plot(time, cleanangles)
    peaksseries = find_peaks(x, distance=50)[0]
    times = []
    for i in range(len(peaksseries) - 1):
        differencetime = int(peaksseries[i+1]) - int(peaksseries[i])
        times.append(differencetime)
    averagetime = sum(times)/len(times)
    period = averagetime
    return period
    
def plot_accelerationx_time(time, x):
    # plots the acceleration of the pendulum in the x direction as a function
    # of time, with vertical and horizontal axis titles and a plot title.
    # takes arrays of time and x acceleration.
    # void function.
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("X Acceleration")
    plt.title("X Acceleration vs. Time")
    plt.plot(time, x)
    plt.show()

def plot_accelerationy_time(time, y):
    # plots the acceleration of the pendulum in the y direction as a function
    # of time, with vertical and horizontal axis titles and a plot title.
    # takes arrays of time and y acceleration.
    # void function.
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Y Acceleration")
    plt.title("Y Acceleration vs. Time")
    plt.plot(time, y)
    plt.show()
    
def plot_accelerationz_time(time, z):
    # plots the acceleration of the pendulum in the z direction as a function
    # of time, with vertical and horizontal axis titles and a plot title.
    # takes arrays of time and z acceleration.
    # void function.
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Z Acceleration")
    plt.title("Z Acceleration vs. Time")
    plt.plot(time, z)
    plt.show()
 
def plot_theta_time(time, x, y):
    # plots the angle theta in degrees of the pendulum as a function of time,
    # with vertical and horizontal axis titles and a plot title.
    # takes arrays of time, x acceleration, and y acceleration.
    # void function.
    plt.xlabel("Time (milliseconds)")
    plt.ylabel("Angle (degrees)")
    plt.title("Theta vs. Time")
    angleseries = find_theta(x, y)
    plt.plot(time, angleseries)

def plot_all():
    # combines all plotting functions above in order to plot all three
    # accelerations as well as angles for a certain length at once.
    # takes no arguments, void function. 
    plot_accelerationx_time(timeseries, xseries)
    plot_accelerationy_time(timeseries, yseries)
    plot_accelerationz_time(timeseries, zseries)
    plot_theta_time(timeseries, xseries, yseries)
    
def plot_periods(length, period):
    # plots the periods of the pendulum as a function of length of the pendulum
    # takes arrays of lengths of pendulums and corresponding periods found
    # from calculations.
    # void function.
    plt.xlabel("Length (cm)")
    plt.ylabel("Period (seconds)")
    plt.title("Period vs. Length of Pendulum")
    plt.plot(length, period)
    plt.show()

xseries = []   
for row in newarray:
    xseries.append(int(row[0]))
    sp.signal.medfilt(xseries)

yseries = []
for row in newarray:
    yseries.append(int(row[1]))
    sp.signal.medfilt(yseries)

zseries = []
for row in newarray:
    zseries.append(int(row[2]))
    sp.signal.medfilt(zseries)

timeseries = []
for row in newarray:
    timeseries.append(int(row[3]))
    sp.signal.medfilt(timeseries)
    
lengthseries = [18, 24.5, 31.5, 39, 48.5]
periodseries = [0.59, 0.61, 0.545, 0.69, 0.52]

plot_all()