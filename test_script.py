import numpy as np

from utils import get_tolerance_factor

def test_stability():
    # Test values: Cs=1.88, Sn=1.1, X=2.2
    t = get_tolerance_factor(1.88, 1.1, 2.2)
    
    # Check if calculation is correct (Expect approx 0.94)
    assert 0.8 <= t <= 1.1, f"Stability logic test failed! Calculated t = {t}"
    print(f"Tests passed successfully! Tolerance Factor: {t:.4f}")

if __name__ == "__main__":
    test_stability()
