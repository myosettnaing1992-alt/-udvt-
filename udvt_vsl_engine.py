import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MyoConsistencyEngine:
    """
    UDVT v3.0 - Variable Speed of Light (VSL) & Hubble Tension Engine
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038, h0_local=73.04, omega_m=0.315):
        self.beta = beta
        self.h0 = h0_local          # Local measurement (SH0ES)
        self.omega_m = omega_m
        self.omega_lambda = 1 - omega_m
        self.c0 = 299792458         # Speed of light today (m/s)

    def vsl_factor(self, z):
        """Variable Speed of Light factor c(z) = c0 * (1 + z)^beta"""
        return (1 + z)**self.beta

    def udvt_h_z(self, z):
        """Modified Hubble parameter H(z) with VSL correction"""
        v_factor = self.vsl_factor(z)
        # UDVT correction: Dynamic vacuum term modulated by VSL
        h_sq = self.h0**2 * (self.omega_m * (1+z)**3 + self.omega_lambda * (v_factor**2))
        return np.sqrt(h_sq)

    def lcdm_h_z(self, z, h0_planck=67.4):
        """Standard LCDM H(z) for comparison (Planck baseline)"""
        h_sq = h0_planck**2 * (self.omega_m * (1+z)**3 + (1 - self.omega_m))
        return np.sqrt(h_sq)

    def generate_tension_report(self, z_max=3.0):
        """Generates comparison report between UDVT and LCDM"""
        z_vals = np.linspace(0, z_max, 100)
        h_udvt = [self.udvt_h_z(z) for z in z_vals]
        h_lcdm = [self.lcdm_h_z(z) for z in z_vals]
        
        df = pd.DataFrame({
            'Redshift_z': z_vals,
            'H_UDVT': h_udvt,
            'H_LCDM': h_lcdm,
            'Difference_Percent': (np.array(h_udvt) - np.array(h_lcdm)) / np.array(h_lcdm) * 100
        })
        return df

def plot_hubble_evolution():
    engine = MyoConsistencyEngine()
    z = np.linspace(0, 2.5, 500)
    
    h_u = [engine.udvt_h_z(zi) for zi in z]
    h_l = [engine.lcdm_h_z(zi) for zi in z]
    
    plt.figure(figsize=(10, 6))
    plt.plot(z, h_u, label='UDVT H(z) (with VSL & local H0)', color='darkred', lw=2.5)
    plt.plot(z, h_l, '--', label='Standard LCDM H(z) (Planck H0)', color='navy', alpha=0.7)
    
    plt.title("Hubble Tension Resolution: UDVT vs Standard LCDM", fontsize=14)
    plt.xlabel("Redshift (z)", fontsize=12)
    plt.ylabel("H(z) [km/s/Mpc]", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Highlight the H0 convergence
    plt.annotate(f'Local H0: {engine.h0}', xy=(0, engine.h0), xytext=(0.5, engine.h0 + 20),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.savefig("UDVT_Hubble_Tension_Resolution.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    engine = MyoConsistencyEngine()
    report = engine.generate_tension_report()
    report.to_excel("UDVT_Hubble_Consistency_Results.xlsx", index=False)
    plot_hubble_evolution()
    print("Success: VSL-based Hubble analysis complete.")
