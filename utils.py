import numpy as np

def get_tolerance_factor(r_a, r_b, r_x):
    """Calculates Goldschmidt Tolerance Factor"""
    return (r_a + r_x) / (np.sqrt(2) * (r_b + r_x))

def get_octahedral_factor(r_b, r_x):
    """Calculates Octahedral Factor"""
    return r_b / r_x
