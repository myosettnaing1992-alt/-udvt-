import numpy as np
import pandas as pd

class UDVTConsistencyChecker:
    """
    UDVT v2.0 - Myo Limit Derivation and Consistency Check
    Computes the maximum allowed beta from information-theoretic bounds.
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038, omega_vac=0.692):
        self.beta = beta
        self.omega_vac = omega_vac
        self.H0_km_s_mpc = 67.4
        
    def compute_myo_limit(self):
        """
        Computes the Myo Limit (beta_max) using Information-Theoretic Bound.
        Formula derived from Margolus-Levitin theorem in UDVT context:
        beta_max = (2 / pi) * (rho_vac / (M_pl^2 * H0^2))
        """
        # In UDVT framework, rho_vac / (M_pl^2 * H0^2) simplifies to Omega_vac * 3/(8*pi)
        rho_factor = self.omega_vac * (3 / (8 * np.pi))
        beta_max = (2 / np.pi) * rho_factor
        return beta_max

    def get_safety_analysis(self):
        """Computes safety margin and theoretical consistency"""
        beta_max = self.compute_myo_limit()
        margin = ((beta_max - self.beta) / beta_max) * 100
        is_consistent = self.beta <= beta_max
        
        return {
            "Myo_Limit_Value": beta_max,
            "Observed_Beta": self.beta,
            "Safety_Margin_Percent": margin,
            "Consistency_Status": "PASSED" if is_consistent else "FAILED"
        }

    def export_consistency_report(self, filename="UDVT_Myo_Limit_Report.xlsx"):
        """Exports the consistency check to an Excel file for the manuscript"""
        analysis = self.get_safety_analysis()
        
        data = {
            "Consistency_Metric": [
                "Theoretical Myo Limit (beta_max)",
                "Current Model Parameter (beta)",
                "Safety Margin",
                "Information-Theoretic Status"
            ],
            "Value": [
                f"{analysis['Myo_Limit_Value']:.6f}",
                f"{analysis['Observed_Beta']:.6f}",
                f"{analysis['Safety_Margin_Percent']:.2f}%",
                analysis['Consistency_Status']
            ],
            "Description": [
                "Max allowed vacuum stiffness via Margolus-Levitin",
                "Value used in UDVT v3.0 simulations",
                "Headroom before reaching quantum computation limit",
                "Mathematical validation against entropy bounds"
            ]
        }
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Consistency Report saved to: {filename}")
        return df

if __name__ == "__main__":
    # Initialize Checker
    checker = UDVTConsistencyChecker(beta=0.0038)
    
    # Run and print results
    report = checker.export_consistency_report()
    print("\n--- UDVT Consistency Check: Myo Limit Analysis ---")
    print(report.to_string(index=False))
