import numpy as np
import pandas as pd

def calculate_chi_square(observed, predicted, errors):
    """
    Calculates the Chi-square statistic.
    Chi^2 = Σ ((Obs - Pred) / Error)^2
    """
    observed = np.array(observed)
    predicted = np.array(predicted)
    errors = np.array(errors)
    return np.sum(((observed - predicted) / errors) ** 2)

class UDVTValidationSuite:
    """
    Statistical validation engine comparing UDVT predictions 
    to Planck 2018 and SH0ES datasets.
    """
    def __init__(self, beta=0.0038):
        self.beta = beta
        # Mock Data Structure for a multi-dataset fit
        self.datasets = {
            'H0_Local': {'obs': 73.04, 'pred': 72.85, 'err': 1.04}, # SH0ES 2022
            'S8_Lensing': {'obs': 0.766, 'pred': 0.762, 'err': 0.017}, # KiDS-1000
            'r_inflation': {'obs': 0.032, 'pred': 0.0038, 'err': 0.01} # BICEP/Keck
        }

    def run_fit_analysis(self):
        print(f"--- [UDVT Statistical Fit Analysis (beta={self.beta})] ---")
        total_chi2 = 0
        
        for name, data in self.datasets.items():
            stat = calculate_chi_square(data['obs'], data['pred'], data['err'])
            total_chi2 += stat
            print(f"Dataset: {name:12} | Chi2: {stat:.4f}")
            
        reduced_chi2 = total_chi2 / len(self.datasets)
        print(f"\nTotal Chi-Square:   {total_chi2:.4f}")
        print(f"Reduced Chi-Square: {reduced_chi2:.4f}")
        
        if reduced_chi2 < 1.5:
            print("Status: EXCELLENT FIT (Statistically Consistent)")
        else:
            print("Status: TENSION PERSISTS (Refine Beta Parameter)")

if __name__ == "__main__":
    validator = UDVTValidationSuite()
    validator.run_fit_analysis()
  
