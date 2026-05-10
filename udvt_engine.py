import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class UDVTEngine:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Core Engine
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038):
        self.beta = beta
        self.G = 6.674e-11
        self.c0 = 299792458
        self.h0_local = 73.04  # km/s/Mpc (SH0ES)
        self.alpha_em = 1/137.036

    def get_hubble_evolution(self, z):
        """Calculates Hubble expansion H(z) with VSL correction."""
        om_m, om_l = 0.315, 0.685
        vsl_correction = (1 + z)**self.beta
        return self.h0_local * np.sqrt(om_m * (1+z)**3 + om_l * vsl_correction**2)

    def get_fermion_masses(self):
        """Topological winding number mass predictions (N=1,2,3)."""
        m_e = 0.000511  # Electron GeV
        gamma = self.beta / self.alpha_em
        return {
            "Electron": m_e,
            "Muon": m_e * np.exp(gamma * 1.037),
            "Tau": m_e * np.exp(gamma * 2 * 1.041)
        }

    def get_rotation_velocity(self, r_kpc, mass_mw=1.2e42):
        """Calculates galactic rotation using vacuum stiffness acceleration."""
        r_m = r_kpc * 3.086e19
        v_newton = np.sqrt((self.G * mass_mw) / r_m) / 1000
        a0 = 1.2e-10 * (self.beta / 0.0038)
        v_udvt = (self.G * mass_mw * a0)**0.25 / 1000
        return np.maximum(v_newton, v_udvt)

    def export_results(self):
        """Exports all numerical data to Excel."""
        z_range = np.linspace(0, 3, 100)
        df = pd.DataFrame({
            'Redshift_z': z_range,
            'H_z_UDVT': [self.get_hubble_evolution(zi) for zi in z_range]
        })
        df.to_excel("UDVT_Simulation_Data.xlsx", index=False)
        print("Data exported to UDVT_Simulation_Data.xlsx")

def run_visuals(engine):
    """Generates the UDVT Evidence Plots."""
    plt.figure(figsize=(12, 5))
    
    # Galactic Dynamics
    plt.subplot(1, 2, 1)
    r = np.linspace(1, 100, 100)
    plt.plot(r, [engine.get_rotation_velocity(ri) for ri in r], label='UDVT Prediction', color='navy')
    plt.axhline(220, color='red', linestyle='--', label='Observed (Flat)')
    plt.title("Galactic Rotation Curves")
    plt.xlabel("Radius (kpc)"); plt.ylabel("Velocity (km/s)"); plt.legend()

    # Hubble Tension
    plt.subplot(1, 2, 2)
    z = np.linspace(0, 2, 100)
    plt.plot(z, [engine.get_hubble_evolution(zi) for zi in z], color='darkgreen')
    plt.title("H(z) Evolution (VSL Corrected)")
    plt.xlabel("Redshift (z)"); plt.ylabel("H(z) [km/s/Mpc]")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    udvt = UDVTEngine()
    print("UDVT Particle Predictions (MeV):")
    for p, m in udvt.get_fermion_masses().items():
        print(f"{p}: {m*1000:.4f}")
    udvt.export_results()
    run_visuals(udvt)
