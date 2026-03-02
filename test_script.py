import numpy as np
# Dono functions ko import kar rahe hain
from utils import get_tolerance_factor, get_octahedral_factor

def test_stability_filters():
    # Test values for a typical perovskite (e.g., CsSnI3)
    r_a, r_b, r_x = 1.88, 1.10, 2.20
    
    # 1. Test Tolerance Factor
    t = get_tolerance_factor(r_a, r_b, r_x)
    assert 0.8 <= t <= 1.1, f"Tolerance factor test failed! Got {t}"
    print(f"✅ Tolerance Factor Test Passed: {t:.4f}")
    
    # 2. Test Octahedral Factor
    mu = get_octahedral_factor(r_b, r_x)
    assert mu > 0.4, f"Octahedral factor test failed! Got {mu}"
    print(f"✅ Octahedral Factor Test Passed: {mu:.4f}")

if __name__ == "__main__":
    print("Starting automated tests...")
    test_stability_filters()
    print("All physics-based filters are working correctly!")
