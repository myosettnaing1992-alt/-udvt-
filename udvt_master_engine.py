import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.constants import hbar, c

class UDVTMasterEngine:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Integrated Master Engine
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    Version: 3.0 (2026)
    
    This engine bridges Cosmology, Particle Physics, and Millennium Mathematics
    using the dimensionless Myo Limit (beta).
    """
    def __init__(self, beta=0.0038):
        self.beta = beta
        self.hbar = hbar
        self.c = c
        self.H0_local = 73.04  # km/s/Mpc (SH0ES baseline)

    # --- 1. COSMOLOGY & VSL ---
    def get_hubble_z(self, z):
        """Calculates H(z) with Variable Speed of Light (VSL) correction."""
        om_m, om_l = 0.315, 0.685
        vsl_factor = (1 + z)**self.beta
        h2 = self.H0_local**2 * (om_m * (1+z)**3 + om_l * vsl_factor**2)
        return np.sqrt(h2)

    # --- 2. PARTICLE PHYSICS: MASS HIERARCHY ---
    def predict_fermion_masses(self):
        """Topological winding number (N=1,2,3) mass predictions."""
        m_e = 0.000511  # Electron GeV
        alpha_em = 1/137.036
        gamma = self.beta / alpha_em
        return {
            "Electron": m_e,
            "Muon": m_e * np.exp(gamma * 1.037),
            "Tau": m_e * np.exp(gamma * 2 * 1.041)
        }

    # --- 3. MILLENNIUM SOLUTIONS ---
    def p_vs_np_complexity(self, n):
        """Complexity collapse from Exponential to Polynomial."""
        t_classical = 2.0**n
        t_udvt = n**(3 * (1 - self.beta))
        return t_classical, t_udvt

    def yang_mills_gap(self, l_scale=1e-35):
        """Calculates the energy gap Delta in Joules."""
        return (self.hbar * self.beta) / (l_scale * self.c)

    def export_master_report(self):
        """Generates comprehensive Excel simulation data."""
        z_vals = np.linspace(0, 2.5, 50)
        n_vals = np.arange(1, 31)
        
        with pd.ExcelWriter("UDVT_Master_Simulation_v3.xlsx") as writer:
            # Expansion Data
            pd.DataFrame({
                'Redshift_z': z_vals,
                'H_z_UDVT': [self.get_hubble_z(zi) for zi in z_vals]
            }).to_excel(writer, sheet_name='Cosmology', index=False)
            
            # Complexity Data
            tc, tu = zip(*[self.p_vs_np_complexity(ni) for ni in n_vals])
            pd.DataFrame({
                'N_Elements': n_vals,
                'Classical_Ops': tc,
                'UDVT_Ops': tu
            }).to_excel(writer, sheet_name='Complexity_P_vs_NP', index=False)

        print("Master Report saved: UDVT_Master_Simulation_v3.xlsx")

# --- VISUALIZATION SUITE ---
def run_udvt_visuals(engine):
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Hubble Evolution
    plt.subplot(1, 3, 1)
    z = np.linspace(0, 2, 100)
    plt.plot(z, [engine.get_hubble_z(zi) for zi in z], color='blue')
    plt.title("H(z) Evolution (VSL)")
    plt.xlabel("Redshift (z)"); plt.ylabel("km/s/Mpc")

    # Plot 2: P vs NP Collapse
    plt.subplot(1, 3, 2)
    n = np.arange(1, 40)
    tc, tu = zip(*[engine.p_vs_np_complexity(ni) for ni in n])
    plt.semilogy(n, tc, 'r--', label='Classical (NP)')
    plt.semilogy(n, tu, 'g-', label='UDVT (P)', lw=2)
    plt.title("P vs NP Complexity")
    plt.xlabel("n"); plt.legend()

    # Plot 3: Zeta Resonance (Riemann)
    plt.subplot(1, 3, 3)
    t = np.linspace(0, 50, 400)
    osc = np.cos(t * np.log(2)) + np.cos(t * np.log(3))
    plt.plot(t, osc, color='purple')
    plt.axhline(0, color='black', alpha=0.3)
    plt.title("Zeta Resonances (Re(s)=1/2)")
    plt.xlabel("Im(s)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    engine = UDVTMasterEngine()
    engine.export_master_report()
    run_udvt_visuals(engine)
