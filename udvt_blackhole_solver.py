import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UDVTBlackHoleDynamics:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Black Hole Module
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    Version: 3.0
    """
    def __init__(self, beta=0.0038):
        self.beta = beta
        self.G = 6.674e-11
        self.c = 3e8
        self.M_sun = 1.989e30

    def schwarzschild_radius(self, mass_kg):
        """Standard Schwarzschild Radius (Event Horizon)"""
        return (2 * self.G * mass_kg) / (self.c**2)

    def udvt_potential(self, mass_kg, r_meters):
        """
        Computes the UDVT Modified Gravitational Potential.
        Resolves the singularity as r approaches zero by using the 
        vacuum stiffness (beta) as a limiting geometric factor.
        """
        rs = self.schwarzschild_radius(mass_kg)
        # UDVT regularizing term to prevent infinite curvature
        r_effective = np.sqrt(r_meters**2 + (self.beta * rs)**2)
        return -(self.G * mass_kg) / r_effective

    def get_lapse_function(self, mass_kg, r_meters):
        """
        Computes the Metric Lapse Function f(r).
        In UDVT, f(r) never reaches true zero at the center, 
        implying a 'Frozen Star' or 'Regular Black Hole' structure.
        """
        phi = self.udvt_potential(mass_kg, r_meters)
        return 1 + (2 * phi / self.c**2)

    def generate_bh_report(self, mass_solar_units=10):
        """Generates Black Hole metric data for Excel export"""
        mass_kg = mass_solar_units * self.M_sun
        rs = self.schwarzschild_radius(mass_kg)
        
        # Sampling from outside the horizon to the core
        radii = np.linspace(0, 2 * rs, 100)
        f_udvt = [self.get_lapse_function(mass_kg, r) for r in radii]
        f_gr = [1 - (rs / r) if r > 0 else -np.inf for r in radii]
        
        df = pd.DataFrame({
            'Radius_meters': radii,
            'Radial_Distance_units_of_Rs': radii / rs,
            'UDVT_Metric_f_r': f_udvt,
            'Standard_GR_f_r': f_gr
        })
        return df

def plot_black_hole_resolution():
    sim = UDVTBlackHoleDynamics()
    mass_bh = 5 * sim.M_sun
    rs = sim.schwarzschild_radius(mass_bh)
    
    radii = np.linspace(0.01 * rs, 2 * rs, 500)
    f_u = [sim.get_lapse_function(mass_bh, r) for r in radii]
    f_g = [1 - (rs / r) for r in radii]
    
    plt.figure(figsize=(10, 6))
    plt.plot(radii/rs, f_u, label='UDVT Regular Black Hole (Singularity Resolved)', color='darkred', lw=2.5)
    plt.plot(radii/rs, f_g, '--', label='Standard Schwarzschild (Singularity at r=0)', color='black', alpha=0.5)
    
    plt.axhline(0, color='blue', linestyle=':', label='Event Horizon Threshold')
    plt.title("Black Hole Metric Potential: UDVT vs General Relativity", fontsize=14)
    plt.xlabel("Radius (r / Rs)", fontsize=12)
    plt.ylabel("Metric Coefficient f(r)", fontsize=12)
    plt.ylim(-1.5, 1.2)
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.savefig("UDVT_BlackHole_Resolution.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    # 1. Visualization
    plot_black_hole_resolution()
    
    # 2. Excel Export
    sim = UDVTBlackHoleDynamics()
    bh_report = sim.generate_bh_report()
    bh_report.to_excel("UDVT_BlackHole_Dynamics_Results.xlsx", index=False)
    print("Success: Black Hole simulation exported to UDVT_BlackHole_Dynamics_Results.xlsx")
