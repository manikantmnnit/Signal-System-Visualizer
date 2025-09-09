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


convolution_properties = {
    "distributive": """
## Distributive Property

The convolution operation is **distributive** over addition:

$$
x[n] * (h_1[n] + h_2[n]) = x[n] * h_1[n] + x[n] * h_2[n]
$$

### Practical Example
- If a signal passes through two filters in parallel, the total output equals the sum of outputs of each filter separately.

### Notes
- This property allows **splitting a system into smaller parts** and combining outputs.
""",

    "associative": """
## Associative Property

The convolution operation is **associative**:

$$
x[n] * (h_1[n] * h_2[n]) = (x[n] * h_1[n]) * h_2[n]
$$

### Practical Example
- For cascading multiple LTI systems, the order of performing convolutions does not affect the final output.

### Notes
- This property allows **grouping systems in any order** without changing the result.
""",

    "commutative": """
## Commutative Property

The convolution operation is **commutative**:

$$
x[n] * h[n] = h[n] * x[n]
$$

### Practical Example
- The order of the input signal and impulse response does not matter; swapping them gives the same output.

### Notes
- This property is often used in **signal processing algorithms** to simplify computations.
"""
}


convolution_properties_continuous = {
    "distributive": """
## Distributive Property (Continuous-Time)

The convolution operation is **distributive** over addition:

$$
x(t) * (h_1(t) + h_2(t)) = x(t) * h_1(t) + x(t) * h_2(t)
$$

### Practical Example
- If a signal passes through two parallel analog filters, the total output equals the sum of outputs of each filter separately.

### Notes
- This property allows **splitting a continuous-time system into smaller parts** and combining outputs.
""",

    "associative": """
## Associative Property (Continuous-Time)

The convolution operation is **associative**:

$$
x(t) * (h_1(t) * h_2(t)) = (x(t) * h_1(t)) * h_2(t)
$$

### Practical Example
- For cascading multiple continuous-time LTI systems, the order of performing convolutions does not affect the final output.

### Notes
- This property allows **grouping continuous-time systems in any order** without changing the result.
""",

    "commutative": """
## Commutative Property (Continuous-Time)

The convolution operation is **commutative**:

$$
x(t) * h(t) = h(t) * x(t)
$$

### Practical Example
- The order of the input signal and system’s impulse response does not matter; swapping them gives the same output.

### Notes
- This property is often used in **analog signal processing** to simplify computations.
"""
}
