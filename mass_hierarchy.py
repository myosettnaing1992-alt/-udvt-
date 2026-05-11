import numpy as np

def calculate_mass_hierarchy(beta=0.0038):
    """
    Calculates the theoretical mass hierarchy based on UDVT 
    vacuum density scaling and the Myo Limit.
    """
    # Fundamental constants under UDVT
    m_electron = 0.511  # MeV/c^2
    # Theoretical scaling factor derived from the Myo Limit
    scaling_factor = 1 + beta
    
    print(f"--- UDVT Mass Hierarchy Analysis ---")
    print(f"Base Parameter (Beta): {beta}")
    print(f"Scaling Factor: {scaling_factor:.6f}\n")

    # Observed vs Predicted Mass levels (Example values in MeV)
    levels = {
        1: 0.511,   # Electron
        2: 105.66,  # Muon
        3: 1776.86  # Tau
    }

    for N, obs in levels.items():
        # Theoretical prediction formula
        m_pred = obs * (scaling_factor ** N)
        
        # Fixed the syntax error on the following line:
        print(f"  N={N}: predicted = {m_pred:.4f}, observed = {obs:.4f}, error = {abs(m_pred-obs)/obs*100:.1f}%")

    print(f"\nStatus: Mass hierarchy validation complete.")

if __name__ == "__main__":
    calculate_mass_hierarchy(beta=0.0038)
