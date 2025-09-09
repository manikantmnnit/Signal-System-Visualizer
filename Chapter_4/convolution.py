convolution={
"discrete_convolution": """
## Discrete-Time Convolution

Convolution of two discrete-time signals computes the output of a linear time-invariant system.

### Formal Definition
For signals x[n] and h[n]:
$$
y[n] = (x * h)[n] = \sum_{k=-\infty}^{\infty} x[k] \, h[n-k]
$$

### Practical Example
- Digital signal processing: Filtering a discrete audio signal with a finite impulse response (FIR) filter.
- Image processing: Applying a kernel to a 2D image to blur or detect edges (convolution in 2D is an extension).

### Notes
- `x[n]` → input signal  
- `h[n]` → system's impulse response  
- `y[n]` → output signal
""",

    "continuous_convolution": """
## Continuous-Time Convolution

Convolution of two continuous-time signals computes the output of a linear time-invariant system.

### Formal Definition
For signals x(t) and h(t):
$$
y(t) = (x * h)(t) = \int_{-\infty}^{\infty} x(\tau) \, h(t - \tau) \, d\tau
$$

### Practical Example
- Analog circuits: Response of an RC or RLC circuit to an input voltage signal.  
- Audio processing: Applying an echo effect by convolving a sound with an impulse response of a room.

### Notes
- \(x(t)\) → input signal  
- \(h(t)\) → system's impulse response  
- \(y(t)\) → output signal
"""
}
