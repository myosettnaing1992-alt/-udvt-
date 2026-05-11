import pandas as pd
import numpy as np
from scipy.integrate import quad
from astropy.cosmology import Planck18
import astropy.units as u

# Importing your existing repository modules
try:
    import udvt_engine as core
    import growth_sigma8 as growth
    import udvt_visualizer as viz
    import udvt_myo_limit_check as safety
except ImportError as e:
    print(f"Integration Warning: Some modules are missing. Details: {e}")

class UDVTMasterSuite:
    def __init__(self, beta=0.0038):
        # 1. Safety Check: Execute your Myo Limit check immediately
        self.beta = beta
        if hasattr(safety, 'check_limit'):
            safety.check_limit(self.beta)
        
        self.c0 = 299792.458 # Speed of light in km/s
        self.cosmo_ref = Planck18 # Standard Baseline (Astropy)

    def calculate_expansion(self, z_max=1100):
        """
        Uses SciPy to integrate the expansion history based on UDVT parameters.
        """
        print(f"Integrating Expansion History up to z={z_max}...")
        
        def integrand(z):
            # Links to your core engine's Hubble ratio logic
            return 1 / (self.cosmo_ref.H(z).value * (1 + z)**self.beta)

        # High-precision Gaussian quadrature (SciPy)
        comoving_dist, error = quad(integrand, 0, z_max)
        return comoving_dist

    def compile_research_dataframe(self, z_points=None):
        """
        Uses Pandas to structure your simulation data for academic export.
        """
        if z_points is None:
            z_points = np.logspace(-3, 3, 50) # Range from z=0.001 to z=1000

        results = []
        for z in z_points:
            # VSL Calculation
            vsl_c = self.c0 * (1 + z)**self.beta
            
            results.append({
                'Redshift': z,
                'Scale_Factor': 1 / (1 + z),
                'VSL_Velocity_km_s': vsl_c,
                'Standard_H_LCDM': self.cosmo_ref.H(z).value,
                'UDVT_Modified_H': self.cosmo_ref.H(z).value * (1 + z)**self.beta
            })

        return pd.DataFrame(results)

    def execute_workflow(self, export_path="UDVT_V3_Analysis_Report.xlsx"):
        """
        Final Workflow: Compute -> Save to Excel -> Generate Plots
        """
        df = self.compile_research_dataframe()
        
        # Save results for your 'excel-py' processing folder
        df.to_excel(export_path, index=False)
        print(f"Research data successfully exported to {export_path}")

        # Visualization via your 'plotter-py' or 'visualizer' script
        if hasattr(viz, 'generate_plots'):
            viz.generate_plots(df)
            print("Theoretical plots generated.")

# --- Execution Entry ---
if __name__ == "__main__":
    suite = UDVTMasterSuite(beta=0.0038)
    suite.execute_workflow()
  
