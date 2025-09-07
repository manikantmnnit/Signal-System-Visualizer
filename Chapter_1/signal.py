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
    return t, y


def discrete_cos(n, omega=0.1):
    """
    Generate discrete-time cosine signal
    x[n] = cos(ωn)

    """
    t = np.arange(-n, n+1)
    y = np.cos(omega * t)
    return t, y


# create functions for continuous Signals

def Sin(t, dt=0.01):
    """
    Generate Sin signal with resolution dt
    """
    time = np.arange(-t, t, dt)
    y = np.sin(time)
    return time, y

def Cos(t, dt=0.01):
    """
    Generate Cos signal with resolution dt
    """
    time = np.arange(-t, t, dt)
    y = np.cos(time)
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






# ---------------- Common Plot Function ---------------- #

def plot_signal(t, y, 
                plot_type: Literal['plot','stem']='stem',
                title="Discrete Signal", xlabel="n", ylabel="Amplitude",
                line_color='red', marker_color='orange', base_color='black'):
    """
    Common function to plot signals with custom colors
    
    Parameters:
        t, y       : signal data
        plot_type  : 'plot' for continuous, 'stem' for discrete
        title      : plot title
        xlabel     : x-axis label
        ylabel     : y-axis label
        line_color : color of line or stems
        marker_color: color of markers for stem plot
        base_color : color of baseline (for stem)
    """
    fig, ax = plt.subplots(figsize=(8,4))
    
    if plot_type == 'stem':
        ax.stem(t, y, linefmt=line_color, basefmt=base_color)
    elif plot_type == 'plot':
        ax.plot(t, y, color=line_color)
    else:
        raise ValueError("plot_type must be 'plot' or 'stem'")
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    # ax.legend([title])
    
    return fig







