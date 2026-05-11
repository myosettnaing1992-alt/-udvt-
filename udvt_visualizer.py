import numpy as np
import matplotlib.pyplot as plt

class MyoConsistencyEngine:
    """Core physics engine for UDVT consistency checks."""
    def __init__(self, beta=0.0038, h0_udvt=73.0, h0_lcdm=67.4):
        self.beta = beta
        self.h0_udvt = h0_udvt
        self.h0_lcdm = h0_lcdm
        self.om_m = 0.315
        self.om_l = 0.685

    def udvt_h_z(self, z):
        """Hubble parameter with Variable Speed of Light (VSL) correction."""
        vsl_factor = (1 + z)**self.beta
        return self.h0_udvt * np.sqrt(self.om_m * (1+z)**3 + self.om_l * vsl_factor**2)

    def lcdm_h_z(self, z):
        """Standard Lambda-CDM Hubble parameter."""
        return self.h0_lcdm * np.sqrt(self.om_m * (1+z)**3 + self.om_l)

def plot_hubble_tension_resolution():
    engine = MyoConsistencyEngine()
    z_range = np.linspace(0, 2.5, 100)
    
    h_udvt = [engine.udvt_h_z(z) for z in z_range]
    h_lcdm = [engine.lcdm_h_z(z) for z in z_range]

    plt.figure(figsize=(10, 6))
    # Comparison of UDVT and Lambda-CDM Hubble expansion rates
    plt.plot(z_range, h_udvt, 'r-', label=f'UDVT (β={engine.beta}, $H_0$={engine.h0_udvt})', linewidth=2)
    plt.plot(z_range, h_lcdm, 'b--', label=f'$\Lambda$CDM ($H_0$={engine.h0_lcdm})', linewidth=2)
    
    plt.xlabel('Redshift (z)')
    plt.ylabel('H(z) [km/s/Mpc]')
    plt.title('Hubble Tension Resolution: UDVT vs $\Lambda$CDM')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot for the manuscript or GitHub
    plt.savefig("hubble_tension_resolution.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_hubble_tension_resolution()
  
