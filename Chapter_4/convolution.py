import streamlit as st
from scipy import signal
from scipy.signal import fftconvolve

# Continuous Convolution
@st.cache_data
def compute_ct_convolution(x, h, dt, mode="full"):
    
    y = fftconvolve(x, h, mode=mode) * dt
    return y

# discrete convolution
@st.cache_data
def compute_dt_convolution(x, h, mode="full"):
    
    y = fftconvolve(x, h, mode=mode) 
    return y

