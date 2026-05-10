import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class UDVTBackgroundEvolution:
    """
    UDVT v3.0 - Cosmological Background Solver
    Solves the modified Friedmann equation and scalar field evolution.
    Author: Myo Sett Naing (ORCID: 0009-0002-9133-0058)
    """
    def __init__(self, beta=0.0038, Omega_m=0.308, Omega_vac=0.692, kappa=1e-60):
        self.beta = beta
        self.Omega_m = Omega_m
        self.Omega_vac = Omega_vac
        self.kappa = kappa

    def ode_system(self, N, state):
        """
        ODE system for UDVT background in e-folding time N = ln a.
        state[0] = phi (scalar field)
        state[1] = dphi/dN
        """
        phi, dphi_dN = state
        a = np.exp(N)
        
        # Modified Friedmann Equation: H^2 calculation
        # The vacuum term a^(-2*beta) represents the dynamic vacuum evolution
        H_sq = self.Omega_m * a**-3 + self.Omega_vac * a**(-2 * self.beta)
        
        # Modified Klein-Gordon equation component
        # NMDC (Non-Minimal Derivative Coupling) term
        term_nmdc = 3 * self.kappa * H_sq * (dphi_dN**2)
        
        # Second derivative of phi with respect to N
        d2phi_dN2 = -3 * dphi_dN - (2 * self.beta * self.Omega_vac * a**(-2 * self.beta)) / (H_sq * (1 + term_nmdc))
        
        return [dphi_dN, d2phi_dN2]

    def run_evolution(self, N_end=5.0):
        """Runs the integration from N=0 (today) to N_end (future)"""
        N_span = (0, N_end)
        initial_state = [0.1, -self.beta] # phi_0, dphi/dN_0
        
        t_eval = np.linspace(0, N_end, 100)
        sol = solve_ivp(self.ode_system, N_span, initial_state, t_eval=t_eval, rtol=1e-8)
        
        # Calculating Hubble evolution for results
        a_vals = np.exp(sol.t)
        H_sq_vals = self.Omega_m * a_vals**-3 + self.Omega_vac * a_vals**(-2 * self.beta)
        
        df_results = pd.DataFrame({
            'e_folding_N': sol.t,
            'Scale_Factor_a': a_vals,
            'Scalar_Field_phi': sol.y[0],
            'dphi_dN': sol.y[1],
            'H_squared': H_sq_vals
        })
        return df_results

    def export_results(self, filename="UDVT_Background_Evolution.xlsx"):
        df = self.run_evolution()
        df.to_excel(filename, index=False)
        print(f"Success: Evolution data exported to {filename}")

def plot_background_results(df):
    plt.figure(figsize=(10, 5))
    
    # Plotting Scalar Field
    plt.subplot(1, 2, 1)
    plt.plot(df['e_folding_N'], df['Scalar_Field_phi'], color='blue', label='$\phi(N)$')
    plt.title('Scalar Field Evolution')
    plt.xlabel('e-folding time (N)')
    plt.ylabel('$\phi$')
    plt.grid(True, alpha=0.3)
    
    # Plotting Hubble Parameter Squared
    plt.subplot(1, 2, 2)
    plt.plot(df['e_folding_N'], df['H_squared'], color='red', label='$H^2(N)$')
    plt.yscale('log')
    plt.title('Expansion Rate ($H^2$)')
    plt.xlabel('e-folding time (N)')
    plt.ylabel('$H^2$ (Normalized)')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    solver = UDVTBackgroundEvolution()
    results = solver.run_evolution()
    solver.export_results()
    plot_background_results(results)
