import streamlit as st
import numpy as np
from Chapter_1.signal import unit_step, ramp, unit_impulse, exponential,  Sin, Cos,Exponential,discrete_cos,discrete_sin, get_signal
from backend import plot_signal
import uuid
from uuid import uuid4


# ---------------------------------------------

# Initialize session state for chapter and signal selection
if "chapter" not in st.session_state:
    st.session_state.chapter = None
if "signal_mode" not in st.session_state:
    st.session_state.signal = None
if 'parameters' not in st.session_state:
    st.session_state.parameters=None

if 'signal_choice' not in st.session_state:
    st.session_state.signal_choice=None

if 'system' not in st.session_state:
    st.session_state.system=None

if 'signal_delay' not in st.session_state:
    st.session_state.signal_delay=0





# Title at the top
st.title("Signal and System Using Python and Chatbot")


# ------------------------define helping functions------------------

def get_discrete_input(key_suffix="main"):
    return st.number_input(
        label="Enter the discrete number",
        min_value=1, max_value=100,
        value=10, step=1,
        key=f"discrete_input_{key_suffix}"   # stable key
    )

def get_continuous_input():
    return st.slider("Select time range",
                      0.0, 100.0, 10.0, 0.01,
                      key="continuous_input")

def get_discrete_delayed(key_suffix="delay"):
    return st.slider(
        label="Enter the discrete delay",
        min_value=-20, max_value=20,
        value=10, step=1,
        key=f"discrete_delay_{key_suffix}"
    )

def get_continuous_delayed():
    return st.slider("Select Delay Range", -10.0, 10.0, 10.0, 0.01,
                     key="continuous_delay")

# -------- sidebar for navigation --------
chapter1_selected = st.sidebar.button("Chapter 1: Signal Plots")
if chapter1_selected:
    st.session_state.chapter = "Chapter 1"




# chapter 2 button
chapter2_selected=st.sidebar.button("Chapter 2: System Selection")
if chapter2_selected:
    st.session_state.chapter = "Chapter 2"

# chapter 3 button
chapter3_selected=st.sidebar.button("Chapter 3: System Properties") 
if chapter3_selected:
    st.session_state.chapter = "Chapter 3"

# ----------------main Content
if st.session_state.chapter=='Chapter 1':
    st.header('Basic Signal Plots')


    # create 2 columns
    col1,col2=st.columns(2)
    with col1:

        st.session_state.signal_mode=st.radio(
            " select a signal mode",
            ( "Discrete","Continuous")
            )
    with col2:
        if st.session_state.signal_mode=='Discrete':
            st.session_state.signal_choice=st.radio('select the Discrete signal',
                 ("unit step", "unit impulse", "ramp", "exponential","sin","cos"))
            st.session_state.parameters =get_discrete_input()

            
            # generate signal and visualize 
            t, y = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
            st.pyplot(plot_signal(t, y, title=f"{st.session_state.signal_choice} Signal"))


            
        if st.session_state.signal_mode=='Continuous':
            st.session_state.signal_choice=st.radio('select continuous Signal',
                                   ('Sin','Cos','Exponential'))
            st.session_state.parameters = get_continuous_input()

            # generate signal and visualize 
            t, y = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
            st.pyplot(plot_signal(t, y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))
    
   
# ------------Chapter 2 : System Selection

if st.session_state.chapter=='Chapter 2':
    st.header('System Analysis on Discrete or Continuous Signals') 

    col1, col2, col3=st.columns(3)  

    with col1:
        st.session_state.signal_mode=st.radio(
            " select a signal mode",
            ( "Discrete","Continuous")
            )

    with col2:
        if st.session_state.signal_mode=='Discrete':
            st.session_state.signal_choice=st.radio('select the Discrete signal',
                 ("unit step", "unit impulse", "ramp", "exponential","sin","cos"))
            st.session_state.parameters =get_discrete_input()

            
            # generate signal and visualize 
            t, y = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
            st.pyplot(plot_signal(t, y, title=f"{st.session_state.signal_choice} Signal"))


            
        if st.session_state.signal_mode=='Continuous':
            st.session_state.signal_choice=st.radio('select continuous Signal',
                                   ('Sin','Cos','Exponential'))
            st.session_state.parameters = get_continuous_input()

            # generate signal and visualize 
            
            t, y = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
            st.pyplot(plot_signal(t, y, plot_type='plot', title=f"{st.session_state.signal_choice} Signal"))

    with col3:
        st.session_state.system = st.radio(
            " select a system",
            ("Time Scaling", "Amplitude Scaling","Delay", "Reverse", "Square")
        )

        if st.session_state.signal_mode=='Discrete' and st.session_state.signal_choice and st.session_state.parameters:

            # Reverse
            if st.session_state.system=='Reverse':
                st.header('Reverse')
                st.pyplot(plot_signal(t, -y, title=f"{st.session_state.signal_choice} Signal"))

            # Square
            if st.session_state.system=='Square':
                st.header('Square')
                st.pyplot(plot_signal(t, y*y, title=f"{st.session_state.signal_choice} Signal"))

            # for time scaling
            if st.session_state.system=="Time Scaling":
                # define delay 
                st.session_state.signal_delay=get_discrete_delayed()
                st.pyplot(plot_signal(st.session_state.signal_delay*t, y, title=f"{st.session_state.signal_choice} Signal"))

            if st.session_state.system=="Amplitude Scaling":
                # define delay
                st.session_state.signal_delay=get_discrete_delayed()
                st.pyplot(plot_signal( t, st.session_state.signal_delay*y, title=f"{st.session_state.signal_choice} Signal"))

            # for Delay
            if st.session_state.system=='Delay':
                st.session_state.signal_delay=get_discrete_delayed()
                st.pyplot(plot_signal(t-st.session_state.signal_delay, y, title=f"{st.session_state.signal_choice} Signal"))

            

        if st.session_state.signal_mode=='Continuous' and st.session_state.signal_choice and st.session_state.parameters:

            # Reverse
            if st.session_state.system=='Reverse':
                st.header('Reverse')
                st.pyplot(plot_signal(-t, y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))

            # Square
            if st.session_state.system=='Square':
                st.header('Square')
                st.pyplot(plot_signal(t, y*y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))

            # for time scaling
            if st.session_state.system=="Time Scaling":
                # define delay
                st.session_state.signal_delay=get_continuous_delayed()
                st.pyplot(plot_signal(st.session_state.signal_delay*t, y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))

                # for time scaling
            if st.session_state.system=="Amplitude Scaling":
                # define delay
                st.session_state.signal_delay=get_continuous_delayed()
                st.pyplot(plot_signal(t, st.session_state.signal_delay*y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))

            # for Delay
            if st.session_state.system=='Delay':
                st.session_state.signal_delay=get_continuous_delayed()
                st.pyplot(plot_signal(t-st.session_state.signal_delay, st.session_state.signal_delay*y, plot_type='plot',title=f"{st.session_state.signal_choice} Signal"))

            

        



        


       