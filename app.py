import streamlit as st
import numpy as np
from Chapter_1.signal import unit_step, ramp, unit_impulse, exponential,  Sin, Cos,Exponential,discrete_cos,discrete_sin, get_signal
from backend import plot_signal, plot_and_download
import uuid
from uuid import uuid4
from Chapter_3.system_properties import system_props
from Chapter_4.document_convolution import convolution, convolution_properties, convolution_properties_continuous 
from Chapter_4.convolution import compute_ct_convolution, compute_dt_convolution
from scipy import signal
from scipy.signal import fftconvolve

# make all the columns expand to full scree
st.set_page_config(
    page_title="Signal_system_Visualization",
    layout="wide",      # <-- key part for full width
    initial_sidebar_state="auto"
)
# ---------------------------------------------

# Initialize session state for chapter and signal selection
if "chapter" not in st.session_state:
    st.session_state.chapter = None
if "signal_mode" not in st.session_state:
    st.session_state.signal_mode = None
if 'parameters' not in st.session_state:
    st.session_state.parameters=None

if 'signal_choice' not in st.session_state:
    st.session_state.signal_choice=None

if 'system' not in st.session_state:
    st.session_state.system=None

if 'signal_delay' not in st.session_state:
    st.session_state.signal_delay=0

if "convol_prop" not in st.session_state:
    st.session_state.convol_prop=None





# Title at the top
st.title("Signal and System Using Python and Chatbot")


# ------------------------define helping functions------------------
def get_discrete_input(key_suffix="main"):
    return st.number_input(
        label="Enter the discrete number",
        min_value=1, max_value=100,
        value=10, step=1,
        key=f"discrete_input_{key_suffix}"   
    )

def get_continuous_input(key_suffix="main"):
    return st.slider(
        "Select time range",
        0.0, 100.0, 10.0, 0.01,
        key=f"continuous_input_{key_suffix}"   
    )

def get_discrete_delayed(key_suffix="main"):
    return st.slider(
        label="Enter the discrete delay",
        min_value=-20, max_value=20,
        value=10, step=1,
        key=f"discrete_delay_{key_suffix}"   
    )

def get_continuous_delayed(key_suffix="main"):
    return st.slider(
        "Select Delay Range",
        -10.0, 10.0, 10.0, 0.01,
        key=f"continuous_delay_{key_suffix}"   
    )

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

# Chapter 4 button
chapter4_selected=st.sidebar.button("Chapter 4: Convolution")
if chapter4_selected:
    st.session_state.chapter="Chapter 4"



# Chapter 5 button
chapter5_selected=st.sidebar.button("Chapter 5: Fourier Series")
if chapter5_selected:
    st.session_state.chapter="Chapter 5"

# ----------------main Content
# ------------Chapter 1 :'Basic Signal Plots'
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


# ------------Chapter 3 : System Properties

if st.session_state.chapter=='Chapter 3':

    st.header('Analyse the system properties') 

    col1,col2,col3=st.columns(3)

    with col1:
        st.session_state.signal_mode=st.radio(
            " select a signal mode",
            ( "Discrete","Continuous"),
            key="system_properties_key"
            )

    with col2:
        if st.session_state.signal_mode=='Discrete':
            st.session_state.signal_choice=st.multiselect('select the Discrete signal',
                 ["unit step", "unit impulse", "ramp", "exponential","sin","cos"])
            st.session_state.parameters =get_discrete_input()

            
            # generate signal and visualize 
            for sig_name in st.session_state.signal_choice:
                    t, y = get_signal(sig_name, st.session_state.parameters, st.session_state.signal_mode)
                    
                    fig=plot_signal(t, y, title=f"{sig_name} signal")
                    plot_and_download(fig, filename=f"{sig_name}.png")


            
        if st.session_state.signal_mode=='Continuous':
            st.session_state.signal_choice=st.radio('select continuous Signal',
                                   ('Sin','Cos','Exponential'))
            st.session_state.parameters = get_continuous_input()

            # generate signal and visualize 
            
            t, y = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
            st.pyplot(plot_signal(t, y, plot_type='plot', title=f"{st.session_state.signal_choice} Signal"))
            fig=plot_signal(t, y, title=f"{st.session_state.signal_choice} signal")
            plot_and_download(fig, filename=f"{st.session_state.signal_choice} signal.png")
    with col3:
        select_system_property=st.radio('select System Property',
                                        ("Linearity", "Time Invariance", "Causality", "Stability", "Memory"),
                                        )
       
        if st.session_state.signal_mode=='Discrete' and st.session_state.signal_choice and st.session_state.parameters:
    # Linearity
            if select_system_property=="Linearity":
                with st.expander("Click here for formal definition and example"):
                    st.markdown(system_props["linearity"], unsafe_allow_html=True)

                st.session_state.signal_delay = get_discrete_delayed()

                # --- Step 1: Scaling factor for each selected signal ---
                scale_factors = {}
                for sig_name in st.session_state.signal_choice:
                    scale = st.number_input(f"Scaling factor for {sig_name}", value=1, step=1)
                    scale_factors[sig_name] = scale

                
                combined_y = None
                t_array = None

                for sig_name in st.session_state.signal_choice:
                    t, y = get_signal(sig_name, st.session_state.parameters, st.session_state.signal_mode)

                    # Apply scaling and optional delay
                    y_scaled = np.array(y) * scale_factors[sig_name]
                    
                    # Sum signals
                    if combined_y is None:
                        combined_y = y_scaled
                        t_array = t
                    else:
                        combined_y = combined_y + y_scaled

                # --- Step 3: Plot the combined signal ---
                st.subheader("Combined Scaled Signal")
                st.pyplot(plot_signal(t_array, combined_y, title="Sum of Selected Signals"))

            # Time Invariance

            if select_system_property=="Time Invariance":
                with st.expander("Click here for formal definition and example"):
                    st.markdown(system_props["time_invariance"], unsafe_allow_html=True)

                
            # --- Step 1: Shifting factor factor for each selected signal ---
                shift_factors = {}
                for sig_name in st.session_state.signal_choice:
                    scale = st.number_input(f"Shifting factor for {sig_name}", value=1, step=1)
                    # shift_factors[sig_name] = scale

                    t, y = get_signal(sig_name, st.session_state.parameters, st.session_state.signal_mode)
                    st.pyplot(plot_signal(t-scale, y, title=f"{sig_name} signal"))

            # "Causality"
            if select_system_property=="Causality":
                with st.expander("Click here for formal definition and example"):
                    st.markdown(system_props["causality"], unsafe_allow_html=True)



            # "Stability"

            if select_system_property=="Stability":
                 with st.expander("Click here for formal definition and example"):
                    st.markdown(system_props["stability"], unsafe_allow_html=True)


            # "Memory"
            if select_system_property=="Memory":
                 with st.expander("Click here for formal definition and example"):
                    st.markdown(system_props["memory"], unsafe_allow_html=True)
    


# ------------Chapter 4 : Convolution
if st.session_state.chapter=='Chapter 4':
    row1 = st.container()
    row2 = st.container()
    with row1:

        col1,col2,col3=st.columns(3)

        # define the signal mode

        with col1:
            st.session_state.signal_mode=st.radio(
                " select a signal mode",
                ( "Discrete","Continuous"),
                key="convolution_signal_mode"
                )
            with st.expander("Click for Discrete Convolution"):
                st.markdown(convolution["discrete_convolution"], unsafe_allow_html=True)

            with st.expander("Click for Continuous Convolution"):
                st.markdown(convolution["continuous_convolution"], unsafe_allow_html=True)
        # second  column : input signals 
        with col2:
            if st.session_state.signal_mode=='Discrete':
                st.session_state.signal_choice=st.radio('select the first Discrete signal',
                    ["unit step", "unit impulse", "ramp", "exponential","sin","cos"],
                    key="first_signal")
                
                st.session_state.parameters =get_discrete_input(key_suffix='first_discrete_input')
                
            
                t1, y1 = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
                fig=plot_signal(t1, y1, title=f"{st.session_state.signal_choice} signal")
                plot_and_download(fig, filename=f"first_signal_{st.session_state.signal_choice}.png")

                st.session_state.signal_choice=st.radio('select the second Discrete signal',
                    ["unit step", "unit impulse", "ramp", "exponential","sin","cos"],
                    key="second_signal")
                
                st.session_state.parameters =get_discrete_input(key_suffix='second_discrete_input')
                
            
                t2, y2 = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
                fig=plot_signal(t2, y2, title=f"{st.session_state.signal_choice} signal")
                plot_and_download(fig, filename=f"second_{st.session_state.signal_choice}.png")



                
            if st.session_state.signal_mode=='Continuous':
                st.session_state.signal_choice=st.radio('select first continuous Signal',
                                    ('Sin','Cos','Exponential'),
                                    key='first_continuous_signal')
                st.session_state.parameters = get_continuous_input(key_suffix='first_signal')

                # generate signal and visualize 
                
                t1, y1 = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
                fig = plot_signal(t1, y1, plot_type="plot",title=f"{st.session_state.signal_choice} signal")

                
                plot_and_download(fig, filename=f"first_signal_{st.session_state.signal_choice}.png")
                

                st.session_state.signal_choice=st.radio('select second continuous Signal',
                                    ('Sin','Cos','Exponential'),
                                    key='second_continuous_signal')
                st.session_state.parameters = get_continuous_input(key_suffix='second_signal')

                # generate signal and visualize 
                
                t2, y2 = get_signal(st.session_state.signal_choice, st.session_state.parameters, st.session_state.signal_mode)
                fig = plot_signal(t2, y2, plot_type="plot",title=f"{st.session_state.signal_choice} signal")

                
                plot_and_download(fig, filename=f"second_signal_{st.session_state.signal_choice}.png")
                
            
        with col3:
            st.header('Apply convolution on selected two signals')
            # discrete time : convolution output
            if st.session_state.signal_mode=='Discrete' and st.session_state.signal_choice and st.session_state.parameters:
            
                # m=st.number_input(label='Enter the output index',value=10,step=1)
                # n=st.number_input(label='Enter the dummy index for summation',value=20,step=1)

                result=np.convolve(y1,y2)
                
                t_conv = np.arange(len(result))

                # Plot convolution result
                fig=plot_signal(t_conv, result, plot_type="stem", title="Convolution Result y[n] = x[n] * h[n]")

                plot_and_download(fig, filename=f"discrete_convolution.png")


            # continuous time : convolution output
            if st.session_state.signal_mode=='Continuous' and st.session_state.signal_choice and st.session_state.parameters:
            
                dt = t1[1] - t1[0]  # assume uniform sampling
                    

                y_conv=compute_ct_convolution(y1,y2,dt)
                t_conv = np.arange(0, len(y_conv)*dt, dt)

                # Plot the convolution
                fig_conv = plot_signal(t_conv, y_conv, plot_type="plot", title="Continuous-time Convolution")
                plot_and_download(fig_conv, filename="continuous_time_convolution_result.png")
        st.markdown("---")  # horizontal line
        st.header("### Analysis of Convolution Property")
               

    # ---- Second row ----
    

    with row2:
        col4, col5, col6 = st.columns(3)


        with col4:
            
            st.session_state.signal_mode=st.radio(
                " select a signal mode",
                ( "Discrete","Continuous"),
                key="convolution_property_signal_mode"
                )
            if st.session_state.signal_mode=='Discrete':
                with st.expander("Click for distributive property"):
                    st.markdown(convolution_properties['distributive'], unsafe_allow_html=True)  

                with st.expander("Click for associative property"):
                    st.markdown(convolution_properties['associative'], unsafe_allow_html=True) 

                with st.expander("Click for commutative property"):
                    st.markdown(convolution_properties["commutative"], unsafe_allow_html=True) 
            if st.session_state.signal_mode=='Continuous':
                with st.expander("Click for distributive property"):
                    st.markdown(convolution_properties_continuous['distributive'], unsafe_allow_html=True)  

                with st.expander("Click for associative property"):
                    st.markdown(convolution_properties_continuous['associative'], unsafe_allow_html=True) 

                with st.expander("Click for commutative property"):
                    st.markdown(convolution_properties_continuous["commutative"], unsafe_allow_html=True) 

        with col5:
            if st.session_state.signal_mode=='Discrete':
                selection = st.radio(
                label='Select Convolution Property',
                options=['Distributive (Select 3 signals) ', 'Associative (Select 3 signals)', 'Commutative (Select 2 signals)'],
                key="convolution_property"  
                        )
                
                st.session_state.signal_choice=st.multiselect('select the Discrete signal',
                                        ["unit step", "unit impulse", "ramp", "exponential","sin","cos"])
                st.session_state.parameters =get_discrete_input(key_suffix='x[n]_input')

            
            # generate signal and visualize 
                signals_values = []
                signals_names = st.session_state.signal_choice  

                # First: generate and plot each selected signal
                for sig_name in signals_names:
                    t, y = get_signal(sig_name, st.session_state.parameters, st.session_state.signal_mode)
                    signals_values.append(y)

                    fig = plot_signal(t, y, title=f"{sig_name} signal")
                    plot_and_download(fig, filename=f"{sig_name}.png")

            if st.session_state.signal_mode=='Continuous':
                selection = st.radio(
                label='Select Convolution Property',
                options=['Distributive (Select 3 signals) ', 'Associative (Select 3 signals)', 'Commutative (Select 2 signals)'],
                key="convolution_property"  
                        )
                
                st.session_state.signal_choice=st.multiselect('select the Discrete signal',
                                        ('Sin','Cos','Exponential'))
                st.session_state.parameters =get_continuous_input(key_suffix='x(t)_input')

            
            # generate signal and visualize 
                signals_values = []
                signals_names = st.session_state.signal_choice  

                # First: generate and plot each selected signal
                for sig_name in signals_names:
                    t, y = get_signal(sig_name, st.session_state.parameters, st.session_state.signal_mode)
                    signals_values.append(y)

                    fig = plot_signal(t, y, title=f"{sig_name} signal")
                    plot_and_download(fig, filename=f"{sig_name}.png")

        with col6:
            st.header('Analyse the waveforms using convolution property')

            if st.session_state.signal_mode == 'Continuous' and st.session_state.parameters:
               
                
                dt = t1[1] - t1[0]  # uniform sampling interval

                if selection == 'Commutative (Select 2 signals)':
                    y1 = compute_ct_convolution(signals_values[0], signals_values[1], dt=dt)
                    t1 = np.arange(len(y1)) * dt
                    fig = plot_signal(t1, y1, title="x(t) * h(t)")
                    plot_and_download(fig, filename="x_h_commutative.png")

                    y2 = compute_ct_convolution(signals_values[1], signals_values[0], dt=dt)
                    t2 = np.arange(len(y2)) * dt
                    fig = plot_signal(t2, y2, title="h(t) * x(t)")
                    plot_and_download(fig, filename="h_x_commutative.png")

                elif selection == 'Distributive (Select 3 signals) ':
                    x, h1, h2 = signals_values[:3]

                    # Left side: x(t) * (h1(t) + h2(t))
                    left = compute_ct_convolution(x, np.array(h1) + np.array(h2), dt=dt)
                    t_left = np.arange(len(left)) * dt
                    fig = plot_signal(t_left, left, title="x(t) * (h1(t) + h2(t))")
                    plot_and_download(fig, filename="x_h1h2_distributive_left.png")

                    # Right side: x(t)*h1(t) + x(t)*h2(t)
                    right1 = compute_ct_convolution(x, h1, dt=dt)
                    right2 = compute_ct_convolution(x, h2, dt=dt)
                    right = np.array(right1) + np.array(right2)
                    t_right = np.arange(len(right)) * dt
                    fig = plot_signal(t_right, right, title="x(t)*h1(t) + x(t)*h2(t)")
                    plot_and_download(fig, filename="x_h1h2_distributive_right.png")

                elif selection == 'Associative (Select 3 signals)':
                    x, h1, h2 = signals_values[:3]

                    # Left side: (x(t) * h1(t)) * h2(t)
                    y1 = compute_ct_convolution(x, h1, dt=dt)
                    left = compute_ct_convolution(y1, h2, dt=dt)
                    t_left = np.arange(len(left)) * dt
                    fig = plot_signal(t_left, left, title="(x(t)*h1(t)) * h2(t)")
                    plot_and_download(fig, filename="associative_left.png")

                    # Right side: x(t) * (h1(t) * h2(t))
                    y2 = compute_ct_convolution(h1, h2, dt=dt)
                    right = compute_ct_convolution(x, y2, dt=dt)
                    t_right = np.arange(len(right)) * dt
                    fig = plot_signal(t_right, right, title="x(t) * (h1(t) * h2(t))")
                    plot_and_download(fig, filename="associative_right.png")