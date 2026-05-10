import numpy as np
import pandas as pd

class UDVTParticlePhysics:
    """
    Unified Dynamic Vacuum Theory (UDVT) - Particle Physics Module
    Version: 2.0 (Standard Model Embedding)
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038):
        # Constants
        self.beta = beta
        self.M_pl = 1.22e19          # Planck mass in GeV
        self.v_higgs = 246.0         # Higgs VEV in GeV
        self.alpha_em = 1/137.036    # Fine structure constant
        self.GeV_inv_to_sec = 6.582e-25
        self.sec_to_year = 3.156e7

    def get_gauge_couplings(self, M_GUT=2e16):
        """Computes Gauge couplings at the GUT scale"""
        # SU(3), SU(2), U(1) modes
        modes = {'U1': 1, 'SU2': 3, 'SU3': 8}
        couplings = {}
        for group, n in modes.items():
            g_squared = (self.beta / (4 * np.pi)) * n * (self.M_pl / M_GUT)**2
            couplings[group] = np.sqrt(g_squared)
        return couplings

    def get_ckm_elements(self):
        """Computes approximate CKM matrix elements from UDVT braiding"""
        elements = {
            'V_us': np.exp(-(1**2) * self.beta / self.alpha_em),
            'V_cb': np.exp(-(1**2) * self.beta / self.alpha_em),
            'V_ub': np.exp(-(2**2) * self.beta / self.alpha_em)
        }
        return elements

    def get_neutrino_masses(self, gamma=0.5206):
        """Computes neutrino masses for three generations (eV)"""
        m_base = 0.05
        return {f'N{i}': m_base * np.exp(-gamma * (i-1)) for i in range(1, 4)}

    def get_proton_lifetime(self, m_p=0.938):
        """Computes predicted proton lifetime in years"""
        tau_gev_inv = (self.M_pl**4) / (self.beta**2 * m_p**5)
        tau_years = (tau_gev_inv * self.GeV_inv_to_sec) / self.sec_to_year
        return tau_years

    def get_udviton_mass(self, Lambda_QCD=0.3):
        """Mass of the predicted udviton (light scalar) in eV"""
        m_gev = self.beta * (Lambda_QCD**2) / self.M_pl
        return m_gev * 1e9

    def run_simulation(self):
        """Aggregates all particle physics data"""
        couplings = self.get_gauge_couplings()
        ckm = self.get_ckm_elements()
        neutrinos = self.get_neutrino_masses()
        
        data = {
            "Parameter_Description": [
                "Gauge Coupling U(1) at GUT",
                "Gauge Coupling SU(2) at GUT",
                "Gauge Coupling SU(3) at GUT",
                "CKM Element V_us",
                "CKM Element V_ub",
                "Neutrino Mass N1",
                "Neutrino Mass N3",
                "Proton Lifetime",
                "Udviton Mass"
            ],
            "Value": [
                couplings['U1'], couplings['SU2'], couplings['SU3'],
                ckm['V_us'], ckm['V_ub'],
                neutrinos['N1'], neutrinos['N3'],
                self.get_proton_lifetime(),
                self.get_udviton_mass()
            ],
            "Unit": ["Value", "Value", "Value", "Value", "Value", "eV", "eV", "Years", "eV"]
        }
        return pd.DataFrame(data)

    def export_to_excel(self, filename="UDVT_Particle_Physics_Results.xlsx"):
        df = self.run_simulation()
        df.to_excel(filename, index=False)
        print(f"Success: Results exported to {filename}")

if __name__ == "__main__":
    pp_sim = UDVTParticlePhysics(beta=0.0038)
    results = pp_sim.run_simulation()
    
    print("\n--- UDVT Particle Physics Predictions v2.0 ---")
    print(results.to_string(index=False))
    
    pp_sim.export_to_excel()
