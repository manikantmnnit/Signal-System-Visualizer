import numpy as np
import math
import matplotlib.pyplot as plt
from typing import Literal

def unit_step(n):
    """
    Generate discrete-time unit step signal u[n]
    """
    t = np.arange(-n, n+1)
    y = np.where(t >= 0, 1, 0)
    return t, y

def unit_impulse(n):
    """
    Generate discrete-time unit impulse signal δ[n]
    """
    t = np.arange(-n, n+1)
    y = np.where(t == 0, 1, 0)
    return t, y

def ramp(n):
    """
    Generate discrete-time ramp signal
    """
    t = np.arange(-n, n+1)
    y = np.where(t >= 0, t, 0)
    return t, y

def exponential(n, alpha=0.1):
    """
    Generate discrete-time exponential signal
    x[n] = e^(alpha * n)
    """
    t = np.arange(-n, n+1)
    y = np.exp(alpha * t)
    return t, y



def discrete_sin(n, omega=0.1):
    """
    Generate discrete-time sine signal
    x[n] = sin(ωn)

    """
    t = np.arange(-n, n+1)  
    y = np.sin(omega * t)
    return t, 
def discrete_sin(n, f=1, N=32):
    """
    Generate discrete-time cosine signal
    x[n] = sin(2π f n / N)
    """
    t = np.arange(-n, n+1)
    omega = 2 * np.pi * f / N
    y = np.sin(omega * t)
    return t, y


def discrete_cos(n, f=1, N=32):
    """
    Generate discrete-time cosine signal
    x[n] = cos(2π f n / N)
    """
    t = np.arange(-n, n+1)
    omega = 2 * np.pi * f / N
    y = np.cos(omega * t)
    return t, y


# create functions for continuous Signals

def Sin(t, f=1, dt=0.01):
    """
    Generate continuous-time sin signal
    x(t) = sin(2π f t)
    """
    time = np.arange(-t, t, dt)
    y = np.sin(2 * np.pi * f * time)
    return time, y

def Cos(t, f=1, dt=0.01):
    """
    Generate continuous-time cosine signal
    x(t) = cos(2π f t)
    """
    time = np.arange(-t, t, dt)
    y = np.cos(2 * np.pi * f * time)
    return time, y

def Exponential(t_range, alpha=0.1, dt=0.01):
    """
    Generate continuous-time exponential signal
    x(t) = e^(alpha * t)

    Parameters:
        t_range : positive float, defines [-t_range, t_range]
        alpha   : exponent coefficient (growth/decay)
        dt      : step size for time resolution
    """
    time = np.arange(-t_range, t_range, dt)   # proper time axis
    y = np.exp(alpha * time)
    return time, y


# merge all functions in one function

def get_signal(signal_type, param, mode:Literal["Discrete","Continuous"]="Discrete"):
    """Return (t, y) for the chosen signal."""
    if mode == "Discrete":
        if signal_type == 'unit step':
            return unit_step(param)
        elif signal_type == 'ramp':
            return ramp(param)
        elif signal_type == 'unit impulse':
            return unit_impulse(param)
        elif signal_type == 'exponential':
            return exponential(param, alpha=0.2)
        elif signal_type == 'sin':
            return discrete_sin(param)
        elif signal_type == 'cos':
            return discrete_cos(param)

    elif mode == "Continuous":
        if signal_type == 'Sin':
            return Sin(param)
        elif signal_type == 'Cos':
            return Cos(param)
        elif signal_type == 'Exponential':
            return Exponential(param)

    return None, None







