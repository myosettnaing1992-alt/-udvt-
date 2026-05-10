UDVT v2.0 - Fermion Mass Hierarchy from Winding Numbers
Solves the self-consistent mass equation for generations N=1,2,3.
"""

import numpy as np
from scipy.optimize import fsolve

def mass_from_winding_number(N, beta=0.0038, alpha=1/137.036, m_e=0.000511, include_strong=True, include_weak=True):
    """
    Compute fermion mass for generation N using UDVT scaling.
    
    Parameters:
    N : int - winding number (1,2,3)
    beta : float - vacuum stiffness
    alpha : float - fine-structure constant
    m_e : float - electron mass in GeV
    include_strong : bool - include strong interaction correction
    include_weak : bool - include weak interaction correction
    
    Returns:
    mass : float - mass in GeV
    """
    gamma0 = beta / alpha  # ~0.5206
    
    if N == 1:
        return m_e
    
    def equation(m):
        m_GeV = m
        correction = 1.0
        if include_strong:
            alpha_s = 0.118
            correction += alpha_s / np.pi
        if include_weak:
            G_F = 1.166e-5  # GeV^{-2}
            correction += G_F * m_GeV**2
        return m - m_e * np.exp(gamma0 * (N-1) * correction)
    
    m_guess = m_e * np.exp(gamma0 * (N-1))
    mass = fsolve(equation, m_guess)[0]
    return mass

# Observed masses (GeV)
observed = {1: 0.000511, 2: 0.1057, 3: 1.777}

if __name__ == "__main__":
    print("UDVT Fermion Mass Predictions (GeV):")
    for N in [1,2,3]:
        m_pred = mass_from_winding_number(N)
        obs = observed[N]
        print(f"  N={N}: predicted = {m_pred:.4f}, observed = {obs:.4f}, error = {abs(m_pred-obs)/obs*100:.1f}%")