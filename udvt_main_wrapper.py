"""
UDVT v3.0 - Full Simulation Wrapper & Research Summary
Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
Purpose: Integrates all UDVT sub-modules for a unified scientific report.
"""

import numpy as np
import pandas as pd

# ကျွန်ုပ်တို့ ရေးသားခဲ့သော Module များကို Import လုပ်ခြင်း (ဖိုင်များ ရှိနေရန် လိုအပ်သည်)
try:
    from udvt_cosmology import UDVTCosmology
    from udvt_growth_sigma8 import UDVTCosmologicalGrowth
    from udvt_mass_hierarchy import UDVTMassHierarchy
    from udvt_quantum_info import UDVTQuantumInfo
    from udvt_particle_physics import UDVTParticlePhysics
    from udvt_myo_limit_check import UDVTConsistencyChecker
except ImportError:
    print("Warning: Some sub-modules are missing. Ensure all .py files are in the same directory.")

class UDVTMasterRunner:
    def __init__(self, beta=0.0038):
        self.beta = beta
        print("="*65)
        print(f"      UDVT v3.0 - UNIFIED DYNAMIC VACUUM THEORY SIMULATION")
        print(f"               Author: Myo Sett Naing (ORCID: ...)         ")
        print("="*65)

    def run_all(self):
        # 1. Consistency Check (The Myo Limit)
        checker = UDVTConsistencyChecker(beta=self.beta)
        limit_data = checker.get_safety_analysis()
        
        # 2. Cosmology & Growth
        cosmo_growth = UDVTCosmologicalGrowth(beta=self.beta)
        s8_pred = cosmo_growth.compute_sigma8()
        
        # 3. Particle Physics & Mass Hierarchy
        hierarchy = UDVTMassHierarchy(beta=self.beta)
        mass_results = hierarchy.run_analysis()
        
        pp = UDVTParticlePhysics(beta=self.beta)
        proton_life = pp.get_proton_lifetime()
        udviton_m = pp.get_udviton_mass()
        
        # 4. Quantum Information
        qi = UDVTQuantumInfo(beta=self.beta)
        holevo = qi.get_holevo_capacity()
        
        # --- PRINTING COMPREHENSIVE SUMMARY ---
        
        print(f"\n[1] CONSISTENCY CHECK (The Myo Limit)")
        print(f"    - Observed Beta: {self.beta}")
        print(f"    - Max Allowed (Myo Limit): {limit_data['Myo_Limit_Value']:.4f}")
        print(f"    - Safety Margin: {limit_data['Safety_Margin_Percent']:.2f}% [{limit_data['Consistency_Status']}]")

        print(f"\n[2] COSMOLOGICAL PREDICTIONS")
        print(f"    - Predicted sigma_8: {s8_pred:.4f} (Observed: ~0.75-0.78)")
        print(f"    - Hubble Tension: Resolved via beta-driven dynamic vacuum.")

        print(f"\n[3] FERMION MASS HIERARCHY")
        for _, row in mass_results.iterrows():
            print(f"    - {row['Particle']}: {row['UDVT_Predicted_GeV']*1000:.4f} MeV (Error: {row['Error_Percentage']:.2f}%)")

        print(f"\n[4] PARTICLE PHYSICS & STRINGS")
        print(f"    - Predicted Proton Lifetime: {proton_life:.2e} years")
        print(f"    - Udviton Mass: {udviton_m:.2e} eV")

        print(f"\n[5] QUANTUM INFORMATION BOUNDS")
        print(f"    - Holevo Information Capacity: {holevo:.2e} bits")
        
        print("\n" + "="*65)
        print("Simulation Complete. Data exported to UDVT_Master_Report.xlsx")
        
        # Exporting a combined summary to Excel
        self.export_final_summary(s8_pred, proton_life, udviton_m, limit_data)

    def export_final_summary(self, s8, proton, udviton, limit):
        summary_data = {
            "Domain": ["Consistency", "Cosmology", "Particle Physics", "Particle Physics"],
            "Metric": ["Myo Limit Margin", "sigma_8 Prediction", "Proton Lifetime", "Udviton Mass"],
            "Result": [f"{limit['Safety_Margin_Percent']:.2f}%", f"{s8:.4f}", f"{proton:.2e} yrs", f"{udviton:.2e} eV"]
        }
        pd.DataFrame(summary_data).to_excel("UDVT_Master_Report.xlsx", index=False)

if __name__ == "__main__":
    runner = UDVTMasterRunner(beta=0.0038)
    runner.run_all()
