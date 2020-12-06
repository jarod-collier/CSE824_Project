import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

#Graphing code from https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly

def fitted_curve(x, a):
    return x**a

def curve_fit_network_in(filename, start_index, end_index):
    fp = open(filename)
    x=[]
    y=[]
    colors=[]
    for i, line in enumerate(fp):
        if i == 0:#time
            x = line.split(',')[1:]
            x = x[start_index:end_index]
            x = [float(a) for a in x]
        elif i == 2: #number of players
            colors = line.split(',')[1:]
            colors = colors[start_index:end_index]
            colors = [float(a) for a in colors]
        elif i == 6:#network in
            y = line.split(',')[1:]
            y = y[start_index:end_index]
            y = [float(a) for a in y] #convert to megabytes
    x = np.array(x)
    y = np.array(y)
    print(x)
    print(y)
    
    popt, pcov = curve_fit(fitted_curve, x, y)
    
    print("Order of function:",*popt)
    
    #plt.figure(figsize=(5,10))
    #plt.plot(x, y, "ko", label="Data")
    plt.scatter(x, y, c=colors, label="Data")
    plt.plot(x, fitted_curve(x, *popt), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()
    
def curve_fit_cpu(filename, start_index, end_index):
    fp = open(filename)
    x=[]
    y=[]
    colors=[]
    for i, line in enumerate(fp):
        if i == 0:#time
            x = line.split(',')[1:]
            x = x[start_index:end_index]
            x = [float(a) for a in x]
        elif i == 2: #number of players
            colors = line.split(',')[1:]
            colors = colors[start_index:end_index]
            colors = [float(a) for a in colors]
        elif i == 5:#cpu
            y = line.split(',')[1:]
            y = y[start_index:end_index]
            y = [float(a) for a in y]
    x = np.array(x)
    y = np.array(y)
    
    popt, pcov = curve_fit(fitted_curve, x, y)
    
    print("Order of function:",*popt)
    
    plt.figure()
    #plt.plot(x, y, 'ko', label="Data")
    plt.scatter(x, y, c=colors, label="Data")
    plt.plot(x, fitted_curve(x, *popt), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()

#curve_fit_network_in("data/robot_ball.csv", 38, 56)
curve_fit_cpu("data/robot_ball.csv", 38, 56)
#curve_fit_network_in("data/unity_dots.csv", 100, 200)
#curve_fit_cpu("data/unity_dots.csv", 100, 200)