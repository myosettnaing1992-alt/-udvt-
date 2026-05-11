import numpy as np
import matplotlib.pyplot as plt
from astropy.cosmology import Planck18 as cosmo
import udvt_engine as udvt # Importing your core engine

def run_validation_test(beta=0.0038):
    """
    Compares the UDVT expansion history against the Standard LCDM (Planck 2018).
    """
    # 1. Define Redshift range (from local z=0 to cosmic dawn z=2)
    z_range = np.linspace(0, 2, 100)
    
    # 2. Standard Planck 2018 Hubble values (km/s/Mpc)
    h_planck = cosmo.H(z_range).value
    
    # 3. UDVT Modified Hubble values
    # Theoretical Relation: H_udvt = H_planck * (1+z)^beta
    h_udvt = h_planck * (1 + z_range)**beta
    
    # 4. Visualization and Comparison
    plt.figure(figsize=(10, 6))
    plt.plot(z_range, h_planck, 'k--', label='Standard LCDM (Planck18)')
    plt.plot(z_range, h_udvt, 'r-', label=f'UDVT Model (beta={beta})')
    
    plt.title("Hubble Expansion Comparison: UDVT vs Standard LCDM")
    plt.xlabel("Redshift (z)")
    plt.ylabel("Hubble Parameter H(z) [km/s/Mpc]")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 5. Statistical Deviation Analysis
    deviation = ((h_udvt - h_planck) / h_planck) * 100
    print(f"--- UDVT Validation Report ---")
    print(f"Beta Parameter: {beta}")
    print(f"Maximum Deviation at z=2: {deviation[-1]:.2f}%")
    print(f"Hubble Constant H0 (z=0): {h_udvt[0]:.2f} km/s/Mpc")
    
    plt.show()

if __name__ == "__main__":
    run_validation_test()
  
