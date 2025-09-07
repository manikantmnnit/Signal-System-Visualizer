import streamlit as st
import numpy as np
from Chapter_1.signal import unit_step, ramp, unit_impulse, exponential, plot_signal, Sin, Cos,Exponential,discrete_cos,discrete_sin




# ---------------------------------------------

# Initialize session state for chapter and signal selection
if "chapter" not in st.session_state:
    st.session_state.chapter = None
if "signal" not in st.session_state:
    st.session_state.signal = None
if 'parameters' not in st.session_state:
    st.session_state.parameters=None

if 'system' not in st.session_state:
    st.session_state.system=None



# Title at the top
st.title("Signal and System Using Python and Chatbot")


# ------------------------define hepling functions------------------

def get_discrete_input():
    return st.number_input(
        label="Enter the discrete number",
        min_value=1, max_value=100,
        value=10, step=1
    )

def get_continuous_input():
    return st.slider("Select time range", 0.0, 100.0, 10.0, 0.01)

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

        st.session_state.signal=st.radio(
            " select a signal",
            ( "Discrete","Continuous")
            )
    with col2:
        if st.session_state.signal=='Discrete':
            select_signal=st.radio('select the Discrete signal',
                 ("unit step", "unit impulse", "ramp", "exponential","sin","cos"))
            n_input = get_discrete_input()
            st.session_state.parameters = n_input
            
        if st.session_state.signal=='Continuous':
            select_signal=st.radio('select continuous Signal',
                                   ('Sin','Cos','Exponential'))
            t_input= get_continuous_input()
            st.session_state.parameters = t_input
    
   
        
    if select_signal=='unit step':
        t, y = unit_step(n_input)

        st.pyplot(plot_signal(t, y, title="Unit Step u[n]"))
    
    if select_signal=='ramp':
        t, y = ramp(n_input)
        st.pyplot(plot_signal(t, y, title="Ramp x[n]"))

    if select_signal=='unit impulse':
        t, y = unit_impulse(n_input)
        st.pyplot(plot_signal(t, y, title="Unit Impulse δ[n]"))

    if select_signal=='exponential':
        t, y = exponential(n_input, alpha=0.2)
        st.pyplot(plot_signal(t, y, title="Exponential x[n]"))
    
    if select_signal=='sin':
        t, y = discrete_sin(n_input)
        st.pyplot(plot_signal(t, y, title="Sin[n]"))

    if select_signal=='cos':
        t, y = discrete_cos(n_input)
        st.pyplot(plot_signal(t, y, title="Cos[n]"))


    if select_signal=='Sin':
        t,y=Sin(t_input)
        st.pyplot(plot_signal(t=t,y=y,plot_type='plot',title=" Sin(t)",xlabel='t'))
    
    if select_signal=="Cos":
        t,y=Cos(t_input)
        st.pyplot(plot_signal(t=t,y=y,plot_type='plot',title=" Cos(t)",xlabel='t'))

    if select_signal=='Exponential':
        t,y=Exponential(t_input)
        st.pyplot(plot_signal(t=t,y=y,plot_type='plot',title=" e^(alpha*t)",xlabel='t'))

# ------------Chapter 2 : System Selection

if st.session_state.chapter=='Chapter 2':
    st.header('System Analysis on Discrete or Continuous Signals')     

    st.session_state.system=st.radio(
            " select a system",
            ( "Scaling","Delay","Reverse","Square")
            )
    
    if st.session_state.system=='Reverse':
        st.header('Reverse')
    if st.session_state.system=='Delay':
        st.header('Delay')



    

