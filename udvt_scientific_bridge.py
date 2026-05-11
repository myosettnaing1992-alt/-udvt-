import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import minimize
import astropy.units as u
from astropy.cosmology import LambdaCDM, Planck18
import config # Assuming your BETA=0.0038 is here

class UDVTScientificSuite:
    def __init__(self, beta=0.0038):
        self.beta = beta
        # Initialize Astropy cosmology for comparison
        self.reference_cosmo = Planck18 

    def vsl_velocity(self, redshift):
        """Calculates Variable Speed of Light using Astropy Units."""
        z = np.atleast_1d(redshift)
        # c(z) = c0 * (1+z)^beta
        c_now = 299792458 * (u.m / u.s)
        return c_now * (1 + z)**self.beta

    def solve_vacuum_dynamics(self, z_range):
        """Uses SciPy to solve the vacuum energy density evolution."""
        def model(rho, z):
            # Differential equation for vacuum density evolution in UDVT
            # d(rho)/dz - (3 * rho / (1+z)) * (1 - self.beta)
            return (3 * rho / (1 + z)) * (1 - self.beta)

        rho0 = 1.0 # Normalized initial density
        rho_solutions = odeint(model, rho0, z_range)
        return rho_solutions.flatten()

    def generate_research_dataframe(self, z_start=0, z_end=10, points=100):
        """Uses Pandas to structure simulation results for publication."""
        z_values = np.linspace(z_start, z_end, points)
        
        # Calculate parameters
        vsl_values = self.vsl_velocity(z_values).to(u.km / u.s).value
        rho_v = self.solve_vacuum_dynamics(z_values)
        
        # Generate DataFrame
        df = pd.DataFrame({
            'redshift': z_values,
            'vsl_km_s': vsl_values,
            'vacuum_density_norm': rho_v,
            'hubble_standard': [self.reference_cosmo.H(z).value for z in z_values]
        })
        
        # Calculate UDVT specific Hubble (Simplified approximation)
        df['hubble_udvt'] = df['hubble_standard'] * (1 + z_values)**self.beta
        
        return df

# --- Execution Example ---
if __name__ == "__main__":
    suite = UDVTScientificSuite(beta=0.0038)
    
    # Generate simulation data
    results = suite.generate_research_dataframe()
    
    # Display the first 10 rows using Pandas formatting
    print("--- UDVT Cosmological Simulation Results ---")
    print(results.head(10))
    
    # Save to Excel/CSV for your 'excel-py' and 'full-simulations' folders
    # results.to_csv("udvt_v3_results.csv", index=False)
    # results.to_excel("udvt_v3_analysis.xlsx")
  
