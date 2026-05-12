import numpy as np

class UDVT_Cosmology:
    def __init__(self, h=0.732, omega_m=0.28, beta=0.0038):
        """
        UDVT Cosmological Solver
        Default values are optimized for UDVT-Observation Agreement.
        """
        self.H0 = h * 100    # Hubble Constant in km/s/Mpc
        self.Om = omega_m    # Matter Density
        self.Ol = 1 - omega_m # Lambda (Vacuum) Density
        self.beta = beta     # Myo Limit (UDVT Scaling)
        self.c = 299792.458  # Speed of light in km/s

    def hubble_parameter(self, z):
        """
        Calculates H(z) with UDVT VSL correction
        Standard H(z) modified by (1+z)^beta
        """
        h_lcdm = self.H0 * np.sqrt(self.Om * (1 + z)**3 + self.Ol)
        # Apply the UDVT scaling factor to the expansion rate
        return h_lcdm * (1 + z)**self.beta

    def comoving_distance(self, z):
        """
        Calculates the comoving distance D_c(z)
        """
        # Numerical integration for the distance measure
        from scipy.integrate import quad
        integrand = lambda x: self.c / self.hubble_parameter(x)
        dist, _ = quad(integrand, 0, z)
        return dist

    def growth_factor(self, z):
        """
        Calculates the linear growth factor D(z)
        Modified by UDVT to solve S8 Tension
        """
        # Standard growth suppressed by the Beta factor
        standard_growth = 1 / (1 + z)
        suppression = np.exp(-self.beta * z)
        return standard_growth * suppression

    def get_summary(self, z_targets=[0.5, 1.0, 2.0, 1100]):
        """
        Generates a summary of cosmological states at different redshifts
        """
        print(f"{'Redshift (z)':<15} | {'H(z) [km/s/Mpc]':<20} | {'Dist [Mpc]':<15}")
        print("-" * 55)
        for z in z_targets:
            hz = self.hubble_parameter(z)
            dc = self.comoving_distance(z)
            print(f"{z:<15} | {hz:<20.2f} | {dc:<15.2f}")

# --- Execution Block ---
if __name__ == "__main__":
    # Initialize with UDVT parameters
    cosmo = UDVT_Cosmology()
    
    print("--- UDVT Cosmological Engine Report ---")
    print(f"Parameters: H0={cosmo.H0/100}, Omega_m={cosmo.Om}, Beta={cosmo.beta}\n")
    
    cosmo.get_summary()
    
    # S8 Tension Check
    g0 = cosmo.growth_factor(0)
    g1 = cosmo.growth_factor(1.0)
    print(f"\nGrowth Suppression at z=1.0: {((g0-g1)/g0)*100:.2f}%")
  
