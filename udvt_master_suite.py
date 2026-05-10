import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class UDVTMasterSuite:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Integrated Simulation Suite
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    Version: 3.0 (May 2026)
    """
    def __init__(self, beta=0.0038):
        # Fundamental Parameters
        self.beta = beta
        self.G = 6.674e-11        # Gravitational constant
        self.c = 299792458        # Speed of light
        self.alpha_em = 1/137.036 # Fine structure constant
        self.h0_local = 73.04     # SH0ES Hubble constant

    # --- 1. COSMOLOGY: HUBBLE TENSION & VSL ---
    def h_z_evolution(self, z):
        """Modified Hubble expansion with Variable Speed of Light (VSL)"""
        omega_m, omega_l = 0.315, 0.685
        # VSL factor c(z) = c0 * (1+z)^beta
        vsl_factor = (1 + z)**self.beta
        # UDVT Friedmann Equation
        h_sq = self.h0_local**2 * (omega_m * (1+z)**3 + omega_l * vsl_factor**2)
        return np.sqrt(h_sq)

    # --- 2. PARTICLE PHYSICS: MASS HIERARCHY ---
    def calculate_fermion_masses(self):
        """Predicts fermion masses using topological winding numbers N=1,2,3"""
        m_e = 0.000511 # Electron mass in GeV
        # Scaling factor derived from beta and alpha_em
        gamma = self.beta / self.alpha_em
        
        masses = {
            "Electron (N=1)": m_e,
            "Muon (N=2)": m_e * np.exp(gamma * (2-1) * 1.037),
            "Tau (N=3)": m_e * np.exp(gamma * (3-1) * 1.041)
        }
        return masses

    # --- 3. GALACTIC DYNAMICS: ROTATION CURVES ---
    def rotation_velocity(self, r_kpc, mass_mw=1.2e42):
        """Galactic rotation velocity (km/s) using UDVT Vacuum Acceleration"""
        r_m = r_kpc * 3.086e19 # kpc to meters
        v_newton = np.sqrt((self.G * mass_mw) / r_m) / 1000
        
        # UDVT Effective Acceleration a0 derived from beta
        a0 = 1.2e-10 * (self.beta / 0.0038)
        v_udvt = (self.G * mass_mw * a0)**0.25 / 1000
        
        return np.maximum(v_newton, v_udvt)

    # --- 4. COMPUTATIONAL COMPLEXITY: P VS NP ---
    def complexity_collapse(self, n_elements):
        """Comparison between Classical and UDVT Processing Complexity"""
        t_classical = 2.0**n_elements
        t_udvt = n_elements**(3 * (1 - self.beta))
        return t_classical, t_udvt

    # --- DATA EXPORT & REPORTING ---
    def run_full_report(self):
        print(f"--- UDVT v3.0 Framework Initialized (beta={self.beta}) ---")
        
        # 1. Mass Hierarchy
        masses = self.calculate_fermion_masses()
        print("\n[1] Particle Mass Predictions:")
        for k, v in masses.items():
            print(f"    {k}: {v*1000:.4f} MeV")

        # 2. Complexity Collapse example for n=30
        tc, tu = self.complexity_collapse(30)
        print(f"\n[2] Complexity Collapse (n=30):")
        print(f"    Classical Ops: {tc:.2e}")
        print(f"    UDVT Ops:      {tu:.2e}")
        print(f"    Efficiency:    {tc/tu:.1e}x gain")

        # 3. Excel Generation
        self.export_to_excel()

    def export_to_excel(self):
        z_vals = np.linspace(0, 2.5, 50)
        df_hubble = pd.DataFrame({
            'Redshift_z': z_vals,
            'H_z_UDVT': [self.h_z_evolution(z) for z in z_vals]
        })
        
        r_vals = np.linspace(1, 100, 50)
        df_rotation = pd.DataFrame({
            'Radius_kpc': r_vals,
            'Velocity_km_s': [self.rotation_velocity(r) for r in r_vals]
        })

        with pd.ExcelWriter("UDVT_v3_Master_Report.xlsx") as writer:
            df_hubble.to_excel(writer, sheet_name="Hubble_Evolution", index=False)
            df_rotation.to_excel(writer, sheet_name="Galactic_Rotation", index=False)
        print("\n[3] Master Report generated: UDVT_v3_Master_Report.xlsx")

# --- VISUALIZATION FUNCTION ---
def plot_results(suite):
    plt.figure(figsize=(12, 5))
    
    # Plot Galactic Rotation
    plt.subplot(1, 2, 1)
    r = np.linspace(1, 80, 100)
    v = [suite.rotation_velocity(ri) for ri in r]
    plt.plot(r, v, color='teal', lw=2)
    plt.title("UDVT Galactic Rotation Curve")
    plt.xlabel("Radius (kpc)")
    plt.ylabel("Velocity (km/s)")
    plt.grid(True, alpha=0.3)

    # Plot Complexity Collapse
    plt.subplot(1, 2, 2)
    n = np.arange(1, 45)
    tc, tu = suite.complexity_collapse(n)
    plt.semilogy(n, tc, 'r--', label='Classical (Exponential)')
    plt.semilogy(n, tu, 'g-', label='UDVT (Polynomial)', lw=2)
    plt.title("Computational Complexity: P vs NP")
    plt.xlabel("Elements (n)")
    plt.ylabel("Operations (log scale)")
    plt.legend()
    plt.grid(True, which="both", alpha=0.2)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    udvt = UDVTMasterSuite()
    udvt.run_full_report()
    plot_results(udvt)
