fourier_series = {
    "continuous": """
## Continuous-Time Fourier Series (CTFS)

A periodic continuous-time signal \\(x(t)\\) with period \\(T\\) can be expressed as:

$$
x(t) = \\sum_{n=-\\infty}^{\\infty} C_n e^{j n \\omega_0 t}, \\quad \\omega_0 = \\frac{2 \\pi}{T}
$$

### Fourier Coefficients
$$
C_n = \\frac{1}{T} \\int_0^T x(t) e^{-j n \\omega_0 t} dt
$$

### Trigonometric Form
$$
x(t) = a_0 + \\sum_{n=1}^{\\infty} \\big[ a_n \\cos(n \\omega_0 t) + b_n \\sin(n \\omega_0 t) \\big]
$$

### Intuition
- Decomposes a periodic **continuous-time signal** into a sum of sinusoids.
- Shows frequency content at discrete frequencies \\(n \\omega_0\\).
- Used in **signal analysis, filtering, and system response** for periodic signals.

### Key Notes
- Represents **continuous-time periodic signals**.
- Spectrum consists of **discrete harmonics** at multiples of \\(\\omega_0\\).
- Useful for **analog periodic signals** like square waves, sawtooth, etc.

### Example (Square Wave)
$$
x(t) = \\frac{4}{\\pi} \\sum_{n=1,3,5,...}^{\\infty} \\frac{1}{n} \\sin(n \\omega_0 t)
$$
Only odd harmonics are present.
""",

    "discrete": """
## Discrete-Time Fourier Series (DTFS)

A periodic discrete-time signal \\(x[n]\\) with period \\(N\\) can be expressed as:

$$
x[n] = \\sum_{k=0}^{N-1} C_k e^{j 2 \\pi k n / N}
$$

### Fourier Coefficients
$$
C_k = \\frac{1}{N} \\sum_{n=0}^{N-1} x[n] e^{-j 2 \\pi k n / N}, \\quad k=0,1,...,N-1
$$

### Intuition
- Decomposes a periodic **discrete-time signal** into discrete-frequency sinusoids.
- Only \\(N\\) discrete frequency components for period \\(N\\).
- The discrete frequency spectrum is **cyclic (periodic)**.

### Key Notes
- Represents **discrete-time periodic signals**.
- Spectrum contains **N discrete frequency components**.
- DTFS coefficients repeat periodically with period \\(N\\).
- Useful for analyzing **digital periodic signals**.

### Example (8-sample Square Wave)
$$
x[n] = \\{1,1,1,1,-1,-1,-1,-1\\}, \\quad x[n+8]=x[n]
$$
Fourier coefficients:
$$
C_k = \\frac{1}{8} \\sum_{n=0}^7 x[n] e^{-j 2 \\pi k n / 8}
$$
"""
}
