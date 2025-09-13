import numpy as np
from scipy import signal
import pandas as pd

def fourier_coeff(x, N=None):
    """
    Compute all DFS coefficients a_k for a discrete periodic signal.
    """
    x = np.asarray(x)
    if N is None:
        N = len(x)
    n = np.arange(N)
    ak = [(1/N) * np.sum(x * np.exp(-1j * 2 * np.pi * k * n / N)) for k in range(N)]
    return np.array(ak)

def fourier_coeff_table(ak):
    """
    Display Fourier coefficients in a row-wise table format.
    """
    rows = []
    for k, value in enumerate(ak):
        rows.append({
            "k": k,
            "C_k (complex)": f'{np.round(value.real, 2)} + {np.round(value.imag, 2)}j',
            "Magnitude": np.round(np.abs(value), 2),
            "Phase (rad)": np.round(np.angle(value), 2)
        })
    return pd.DataFrame(rows)



def fourier_coeff_continuous(x, t, T, K=20):
    """
    Approximate continuous-time Fourier series coefficients.

    Parameters:
        x : array-like
            Sampled signal over one period [0, T].
        t : array-like
            Time samples corresponding to x.
        T : float
            Fundamental period.
        K : int
            Number of harmonics to compute (symmetric: -K..K).
    Returns:
        ck : np.ndarray
            Fourier coefficients indexed from -K..K.
    """
    dt = t[1] - t[0]  # sample spacing
    k_vals = np.arange(-K, K+1)
    ck = np.array([
        (1/T) * np.sum(x * np.exp(-1j * 2 * np.pi * k * t / T)) * dt
        for k in k_vals
    ])
    return k_vals, ck



def dtfs_synthesis(a_k, N=None):
    """Reconstruct signal x[n] from DTFS coefficients a_k."""
    if N==None:
        N=int(len(a_k))
    k=np.arange(N)
    x_n = [ np.sum(a_k* np.exp(1j * 2 * np.pi *np.arange(N) * n / N)) for n in range(N)]
    return x_n
        

# def ctfs_synthesis(ck, T, t, k_vals):
def ctfs_synthesis(ck, k_vals, t, T):
    """
    Reconstruct signal from Fourier coefficients.
    
    Parameters:
        ck : array-like
            Fourier coefficients
        k_vals : array-like
            Corresponding harmonic indices
        t : array-like
            Time samples for reconstruction
        T : float
            Fundamental period
    
    Returns:
        x_reconstructed : np.ndarray
            Reconstructed signal
    """
    x_reconstructed = np.zeros_like(t, dtype=complex)
    for k, coeff in zip(k_vals, ck):
        x_reconstructed += coeff * np.exp(1j * 2 * np.pi * k * t / T)
    return np.real(x_reconstructed)