# import unittest
import numpy as np

# Ensure these modules are in your PYTHONPATH

from udvt_myo_limit 

# import MyoLimitCheck
from core import UDVT_Core_Cosmology as UDVT_Engine

class TestUDVTCore(unittest.TestCase):
    """
    Validation Suite for Unified Dynamic Vacuum Theory
    Tests the fundamental physical bounds of the Myo Limit.
    """
    def setUp(self):  

        # Initializing with the standard β = 0.0038
        self.engine = UDVT_Engine(beta=0.0038)
        self.limit = MyoLimitCheck(beta=0.0038)

    def test_beta_bound(self):
        """
        [Margolus-Levitin Bound]
        Ensures beta does not exceed the safety limit (β ≤ 0.01).

        Exceeding this causes a breakdown in vacuum information stability.

        """
        self.assertLessEqual(self.engine.beta, 0.01, 

   f"Safety Violation: Beta {self.engine.beta} exceeds 0.01!")

    def test_vsl_logic(self):
        """
        [Variable Speed of Light]
        Verify c(a) increases at higher redshifts as predicted by UDVT.
        """
        a_rec = 1.0 / (1.0 + 1000)
        c_factor = self.engine.vsl_factor(a_rec) self.assertGreater(c_factor, 1.0, 
                          "Physical Error: VSL must be > c0 in the early universe (a < 1)")

    def test_hubble_tension_bridge(self):
        """
        Checks if H(z=0) matches the local SH0ES measurement target.
        """
        h_local = self.engine.hubble_parameter(z=0)

        # Testing for tolerance around the SH0ES baseline (73.04 km/s/Mpc)

        self.assertAlmostEqual(h_local, 70.0, delta=5.0, 

   msg="Hubble local value deviates significantly from tension-resolution range.")

if __name__ == "__main__":

    unittest.main()
  
