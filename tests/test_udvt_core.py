import unittest
import numpy as np

# UDVT Core Scaling Test
def calculate_vsl_scaling(z, beta=0.0038):
    """Calculate Variable Speed of Light scaling factor."""
    return (1 + z)**beta

class TestUDVTCore(unittest.TestCase):
    def test_vsl_at_redshift_zero(self):
        """Test that at z=0, scaling is exactly 1."""
        self.assertEqual(calculate_vsl_scaling(0), 1.0)

    def test_myo_limit_effect(self):
        """Test the effect of Myo Limit (beta) at high redshift."""
        z_high = 1100  # CMB era
        scaling = calculate_vsl_scaling(z_high)
        self.assertGreater(scaling, 1.0)
        print(f"Verified VSL scaling at z=1100: {scaling}")

    def test_vacuum_density_structure(self):
        """Test that vacuum density follows (1+z)^3beta."""
        z = 2.0
        beta = 0.0038
        expected_rho = (1 + z)**(3 * beta)
        self.assertAlmostEqual(calculate_vsl_scaling(z, 3*beta), expected_rho)

if __name__ == '__main__':
    unittest.main()
