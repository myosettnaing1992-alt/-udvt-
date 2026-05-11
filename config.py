"""
UDVT Universal Constants Configuration
This file centralizes all physical constants and theory-specific parameters.
Author: Myo Sett Naing
"""

# --- UDVT Theory Parameters ---
# The Myo-Limit: Dimensionless constant regulating vacuum update rate
# Derived from Margolus-Levitin theorem consistency (beta <= 0.01)
BETA = 0.0038

# Myo-Scale: Characteristic scale for gravity suppression (h/Mpc)
K_MYO = 1.2 

# --- Cosmological Constants (Planck 2018 Base) ---
# Used as the background against which VSL/Disformal effects are calculated
H0_REFERENCE = 67.4  # km/s/Mpc (Global/CMB baseline)
H0_LOCAL_TARGET = 73.04 # km/s/Mpc (SH0ES/Local baseline)
OMEGA_M = 0.315      # Matter density
OMEGA_L = 0.685      # Vacuum density
OMEGA_R = 9.0e-5     # Radiation density (Relativistic species)

# --- Fundamental Physical Constants (SI & GeV) ---
SPEED_OF_LIGHT = 299792458  # m/s (Standard c0)
PLANCK_MASS_GEV = 1.22e19   # Planck Mass in GeV
HBAR = 1.054571817e-34      # Reduced Planck constant (J⋅s)
G_NEWTON = 6.67430e-11      # Gravitational constant (m^3 kg^-1 s^-2)

# --- Derived Theoretical Bounds ---
def get_vsl_at_z(z):
    """Returns the effective speed of light at redshift z."""
    return SPEED_OF_LIGHT * (1 + z)**BETA

def get_vacuum_pressure_correction():
    """Calculates the UDVT vacuum stiffness factor."""
    return 1.0 - BETA
  
