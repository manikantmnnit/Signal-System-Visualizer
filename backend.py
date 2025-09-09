from typing import Literal
import matplotlib.pyplot as plt
import streamlit as st
import io

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

# --------------------------plot and download the image using streamlit
def plot_and_download(fig, filename="signal_plot.png"):
    """
    Display a matplotlib figure in Streamlit and provide a download button.
    
    Args:
        fig: matplotlib.figure.Figure object
        filename: Name of the file to download
    """
    # Show the figure
    st.pyplot(fig)

    # Save figure to buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Download button
    st.download_button(
        label="Download Signal Plot",
        data=buf,
        file_name=filename,
        mime="image/png"
    )