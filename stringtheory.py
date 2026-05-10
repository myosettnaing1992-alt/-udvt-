import numpy as np
import pandas as pd

class UDVTStringTheory:
    """
    Unified Dynamic Vacuum Theory (UDVT) - String Theory Module
    Version: 3.0
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038, h_hubble=0.674):
        # Physical Constants
        self.beta = beta
        self.H0 = (h_hubble * 100 * 1e3) / 3.086e22  # Hubble constant in s^-1
        self.M_pl = 1.22e19                          # Planck mass in GeV
        self.c = 3e8                                 # Speed of light in m/s
        self.seconds_per_year = 3.156e7              # Scaling for time variation

    def get_dilaton_rolling_velocity(self):
        """Computes dilaton field rolling velocity in GeV/s"""
        return np.sqrt(2) * self.beta * self.M_pl * self.H0
    
    def get_internal_volume_drift(self):
        """Computes relative drift rate of internal compactified volume (s^-1)"""
        return self.beta * self.H0
    
    def get_cosmic_string_tension(self):
        """Computes dimensionless cosmic string tension (G mu)"""
        return self.beta**2
    
    def get_tensor_to_scalar_ratio(self):
        """Computes the tensor-to-scalar ratio (r) for CMB B-mode analysis"""
        return 16 * self.beta**2
    
    def get_alpha_variation(self):
        """Computes time variation of the fine-structure constant (yr^-1)"""
        return self.beta * self.H0 * self.seconds_per_year

    def get_regge_slope_shift(self):
        """Computes the vacuum-induced shift in Regge trajectories"""
        return (1 + self.beta)**-1

    def run_full_simulation(self):
        """Aggregates all theoretical predictions into a structured dataset"""
        data = {
            "Physical_Parameter": [
                "Dilaton Rolling Velocity (GeV/s)",
                "Internal Volume Drift (s^-1)",
                "Cosmic String Tension (G_mu)",
                "Tensor-to-Scalar Ratio (r)",
                "Alpha Variation (da/a per year)",
                "Regge Slope Correction Factor"
            ],
            "Value": [
                self.get_dilaton_rolling_velocity(),
                self.get_internal_volume_drift(),
                self.get_cosmic_string_tension(),
                self.get_tensor_to_scalar_ratio(),
                self.get_alpha_variation(),
                self.get_regge_slope_shift()
            ],
            "Unit": ["GeV/s", "s^-1", "Dimensionless", "Ratio", "yr^-1", "Factor"]
        }
        return pd.DataFrame(data)

    def export_to_excel(self, filename="UDVT_String_Theory_Results.xlsx"):
        """Exports the simulation results to a professional Excel file"""
        df = self.run_full_simulation()
        try:
            df.to_excel(filename, index=False)
            print(f"Success: Exported simulation results to {filename}")
        except Exception as e:
            print(f"Error exporting to Excel: {e}")

if __name__ == "__main__":
    # Initialize simulation with UDVT standard beta parameter
    udvt_st = UDVTStringTheory(beta=0.0038)
    
    # Run and display simulation data
    results_df = udvt_st.run_full_simulation()
    print("\n--- UDVT String Theory Simulation v3.0 ---")
    print(results_df.to_string(index=False))
    
    # Export for manuscript / data analysis
    udvt_st.export_to_excel()
