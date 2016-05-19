#Dan Walsh's ODE program file.
#To contain RK4, RK2, Euler, and leapfrog
import numpy as np

def Euler(diffeq, n, y0, t, h):
    """Euler's Method for n ODEs:
        Given y0 at t, returns y1 at t+h"""
    y1 = np.zeros(n)        #start n element array using numpy zeros
    dydt = diffeq(y0,t)     #will give dy/dt at t. assumes dydt is an array
    y1 = y0 + dydt*h    #Euler's method. requires y0 to be n element numpy array
    return y1

def RK2n(diffeq, n, y0, t, h):
    """RK2 method for n ODEs:
        Given y0 at t, returns y1 at t+h"""
    k1 = np.zeros(n)    #initialize, ks and y1 as n element numpy arrays
    k2 = np.zeros(n)
    y1 = np.zeros(n)
    dydt = diffeq(y0, t)    #assumes y0 was created with zeros
    k1 = dydt*h
    k2 = y0 + 0.5*k1
    dydt = diffeq(k2, t+h/2.)
    k2 = dydt*h
    y1 = y0 + k2
    return y1
def RK4n(diffeq, n, y0, t, h):
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    y1 = np.zeros(n)
    dydt = diffeq(y0,t)
    k1 = dydt*h
    dydt = diffeq(y0 + k1/2., t + h/2.)
    k2 = dydt*h
    k3 = diffeq(y0 + k2/2., t + h/2.)*h
    k4 = diffeq(y0 + k3, t+h)*h
    y1 = y0 + k1/6. + (k2 + k3)/3. + k4/6.
    return y1
    
    
