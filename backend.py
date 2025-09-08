from typing import Literal
import matplotlib.pyplot as plt

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


