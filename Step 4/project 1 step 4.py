# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:19:58 2020

@author: moore
"""
import os
import scipy as sp
import numpy
# from numpy import genfromtx


path = "C:/users/moore/mu_code/data_capture"
os.chdir(path)

filename = "length 48.5.csv"


array = np.loadtxt(filename, delimiter=',', dtype=str)
newarray = array.astype('float64')
    
xseries = []   
for row in newarray:
    xseries.append(int(row[0]))
#    sp.signnal.medfilt(xseries)

yseries = []
for row in newarray:
    yseries.append(int(row[1]))
#    sp.signal.medfilt(yseries)

zseries = []
for row in newarray:
    zseries.append(int(row[2]))
#    sp.signal.medfilt(zseries)

timeseries = []
for row in newarray:
    timeseries.append(int(row[3]))
#    sp.signal.medfilt(timseries)

def find_theta(x, y):
    degreesseries = []
    for i in range(len(x)):
        radians = numpy.arctan(y[i]/x[i])
        degrees = 180*radians/numpy.pi
        degreesseries.append(degrees)
    return degreesseries
    
def find_period():
    angleseries = find_theta(xseries, zseries)
#    cleanangles = sp.signal.medfilt(angleseries)
    sp.signal.find_peaks(angleseries)
    
def plot_accelerationx_time(time, x):
    plt.xlabel("Time (seconds)")
    plt.ylabel("X Acceleration")
    plt.title("X Acceleration vs. Time")
    plt.plot(time, x)
    plt.show()

def plot_accelerationy_time(time, y):
    plt.xlabel("Time (seconds)")
    plt.ylabel("Y Acceleration")
    plt.title("Y Acceleration vs. Time")
    plt.plot(time, y)
    plt.show()
    
def plot_accelerationz_time(time, z):
    plt.xlabel("Time (seconds)")
    plt.ylabel("Z Acceleration")
    plt.title("Z Acceleration vs. Time")
    plt.plot(time, z)
    plt.show()
 
def plot_theta_time(time, x, z):
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (degrees)")
    angleseries = find_theta(x, z)
    plt.plot(time, angleseries)
    
plot_accelerationx_time(timeseries, xseries)

# questions:
# finding period
# data quality - medfilt (says scipy does not take signal)
# absolute vs relative path