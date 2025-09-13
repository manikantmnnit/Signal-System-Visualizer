import numpy as np
import math
import matplotlib.pyplot as plt
from typing import Literal
from scipy import signal

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

def discrete_square(n, N=32, duty=0.5):
    """
    Generate discrete-time square wave
    x[n] = square(2πn/N)
    duty: fraction of period signal is high
    """
    t = np.arange(-n, n+1)
    omega = 2 * np.pi / N
    y = signal.square(omega * t, duty=duty)
    return t, y

def discrete_sawtooth(n, N=32, width=1.0):
    """
    Generate discrete-time sawtooth wave
    x[n] = sawtooth(2πn/N)
    width: shape (1.0 -> standard ramp, 0.5 -> symmetric triangle)
    """
    t = np.arange(-n, n+1)
    omega = 2 * np.pi / N
    y = signal.sawtooth(omega * t, width=width)
    return t, y


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

def CT_Square(t_range, f=1, duty=0.5, dt=0.01):
    """
    Generate continuous-time square wave
    """
    time = np.arange(-t_range, t_range, dt)
    y = signal.square(2*np.pi*f*time, duty=duty)
    return time, y

def CT_Sawtooth(t_range, f=1, width=1.0, dt=0.01):
    """
    Generate continuous-time sawtooth wave
    """
    time = np.arange(-t_range, t_range, dt)
    y = signal.sawtooth(2*np.pi*f*time, width=width)
    return time, y

def CT_Cosine(t_range, f=1, dt=0.01):
    """
    Generate continuous-time cosine signal
    """
    time = np.arange(-t_range, t_range, dt)
    y = np.cos(2 * np.pi * f * time)
    return time, y 


# merge all functions in one function

def get_signal(signal_type, param:None, mode:Literal["Discrete","Continuous"]="Discrete",  N_or_T=None):
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
        elif signal_type == "Square":
            return signal.square(2 * np.pi * param / N_or_T)
        elif signal_type  == "Sawtooth":
            return signal.sawtooth(2 * np.pi * param / N_or_T)
        elif signal_type  == "Cosine":
            return np.cos(2 * np.pi * param / N_or_T)

    elif mode == "Continuous":
        if signal_type == 'Sin':
            return Sin(param)
        elif signal_type == 'Cos':
            return Cos(param)
        elif signal_type == 'Exponential':
            return Exponential(param)
        elif signal_type == "Square":
            return signal.square(2 * np.pi * param / N_or_T)
        elif signal_type == "Sawtooth":
            return signal.sawtooth(2 * np.pi * param / N_or_T)
        elif signal_type == "Cosine":
            return np.cos(2 * np.pi * param / N_or_T)

    return None, None  
