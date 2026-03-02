import numpy as np
from utils import calculate_tolerance_factor

def test_stability():
    # Simple test case for stability logic
    t = calculate_tolerance_factor(1.88, 1.1, 2.2)
    assert 0.8 <= t <= 1.1, "Tolerance factor calculation failed"
    print("Tests passed!")

if __name__ == "__main__":
    test_stability()
