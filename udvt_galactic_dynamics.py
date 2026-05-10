import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UDVTGalacticDynamics:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Galactic Rotation Module
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    Version: 3.0
    """
    def __init__(self, beta=0.0038):
        self.beta = beta
        self.G = 6.674e-11  # Gravitational constant
        self.c = 3e8        # Speed of light
        # UDVT specific acceleration scale derived from beta
        self.a0_udvt = 1.2e-10 * (beta / 0.0038) 

    def velocity_newtonian(self, mass_galaxy, radius_kpc):
        """Standard Newtonian orbital velocity (Visible Matter Only)"""
        r_meters = radius_kpc * 3.086e19
        return np.sqrt((self.G * mass_galaxy) / r_meters) / 1000  # unit: km/s

    def velocity_udvt(self, mass_galaxy, radius_kpc):
        """
        UDVT Modified Rotation Velocity using Non-metricity correction.
        Explains flat rotation curves without Dark Matter particles.
        """
        v_n = self.velocity_newtonian(mass_galaxy, radius_kpc)
        v_flat = (self.G * mass_galaxy * self.a0_udvt)**0.25 / 1000
        
        # Interpolation between Newtonian and Deep-UDVT regime
        interpolation = np.sqrt(0.5 + 0.5 * np.sqrt(1 + (4 * v_flat**4 / v_n**4)))
        return v_n * interpolation

    def generate_galactic_report(self, mass_galaxy=1.2e42):
        """Generates galactic rotation data for Excel export"""
        radii = np.linspace(1, 100, 100) # 1 to 100 kpc
        v_newton = [self.velocity_newtonian(mass_galaxy, r) for r in radii]
        v_udvt = [self.velocity_udvt(mass_galaxy, r) for r in radii]
        
        df = pd.DataFrame({
            'Radius_kpc': radii,
            'Newtonian_Velocity_kms': v_newton,
            'UDVT_Predicted_Velocity_kms': v_udvt,
            'Velocity_Difference': np.array(v_udvt) - np.array(v_newton)
        })
        return df

def plot_galactic_rotation():
    sim = UDVTGalacticDynamics()
    radii = np.linspace(1, 100, 100)
    mass_milky_way = 1.2e42 # Approx mass of Milky Way
    
    v_n = [sim.velocity_newtonian(mass_milky_way, r) for r in radii]
    v_u = [sim.velocity_udvt(mass_milky_way, r) for r in radii]
    
    plt.figure(figsize=(10, 6))
    plt.plot(radii, v_u, label='UDVT Prediction (Geometric Effect)', color='teal', lw=2.5)
    plt.plot(radii, v_n, '--', label='Newtonian (Visible Matter Only)', color='orange')
    
    plt.title("Galactic Rotation Curve: UDVT vs Standard Gravity")
    plt.xlabel("Distance from Galactic Center (kpc)")
    plt.ylabel("Orbital Velocity (km/s)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("UDVT_Galactic_Rotation_Plot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    # 1. Visualization
    plot_galactic_rotation()
    
    # 2. Export numerical validation to Excel
    sim = UDVTGalacticDynamics()
    report = sim.generate_galactic_report()
    report.to_excel("UDVT_Galactic_Dynamics_Results.xlsx", index=False)
    print("Success: Galactic simulation exported to UDVT_Galactic_Dynamics_Results.xlsx")
