import numpy as np
import matplotlib.pyplot as plt

class UDVTPhysicsCore:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Physics Engine
    Derivation: Modified Einstein-Hilbert Action (Chapter 4)
    Author: Myo Sett Naing
    """
    def __init__(self, beta=0.0038, k_myo=1.2):
        self.beta = beta
        self.k_myo = k_myo # Myo scale for gravity suppression
        self.G_N = 6.674e-11
        
    def get_disformal_coupling(self, z):
        """
        Calculates B(phi) from the action. 
        In the late-time limit, B(phi) evolves via the Myo Limit.
        """
        return self.beta * np.log(1 + z)

    def get_effective_gravity(self, k, z):
        """
        Implements G_eff(k,t) formula:
        Suppresses gravity at small scales to resolve S8 tension.
        """
        b_phi = self.get_disformal_coupling(z)
        
        # Fundamental UDVT Scale Suppression
        numerator = self.G_N / (1 + b_phi)
        denominator = 1 + (k / self.k_myo)**2
        
        return numerator / denominator

    def simulate_growth_suppression(self):
        """Visualizes the suppression of gravity at different k-scales."""
        k_range = np.logspace(-2, 1, 100)
        g_eff_z0 = [self.get_effective_gravity(ki, 0) / self.G_N for ki in k_range]
        g_eff_z2 = [self.get_effective_gravity(ki, 2) / self.G_N for ki in k_range]

        plt.figure(figsize=(8, 5))
        plt.semilogx(k_range, g_eff_z0, label='z=0 (Current)', color='darkred')
        plt.semilogx(k_range, g_eff_z2, label='z=2 (Early)', color='navy')
        plt.axvline(self.k_myo, color='gray', linestyle='--', label='k_Myo Scale')
        
        plt.title("UDVT Scale-Dependent Gravity Suppression")
        plt.xlabel("Scale k (h/Mpc)")
        plt.ylabel("G_eff / G_Newton")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

# --- Execution ---
if __name__ == "__main__":
    core = UDVTPhysicsCore()
    print(f"Myo-Limit Beta: {core.beta}")
    print(f"Coupling B(phi) at z=1100: {core.get_disformal_coupling(1100):.4f}")
    core.simulate_growth_suppression()
