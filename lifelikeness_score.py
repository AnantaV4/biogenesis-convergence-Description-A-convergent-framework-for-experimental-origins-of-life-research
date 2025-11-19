# lifelikeness_score.py - v0.1 (November 18, 2025)
import numpy as np

def lifelikeness_score(network_cycles=1, persistence_hours=0, dissipation_rate=0, heritability_bits=0):
    """
    Community-editable Lifelikeness Score for protocells / prebiotic systems
    Total score L ∈ [0.0, 4.0]  →  higher = more lifelike
    """
    N = min(np.log10(max(network_cycles, 1)) / 5, 1.0)      # Autocatalytic network complexity
    C = min(persistence_hours / 500.0, 1.0)                 # Compartment lifetime under dilution
    E = min(dissipation_rate / 10.0, 1.0)                   # Energy transduction (kT·s⁻¹·molecule⁻¹)
    H = min(heritability_bits / 8.0, 1.0)                   # Heritable variation (bits)
    return round(N + C + E + H, 3)

# Example calls from real 2020–2025 literature
if __name__ == "__main__":
    print("Empty chemistry →", lifelikeness_score())
    print("Szostak 2023 vesicles →", lifelikeness_score(persistence_hours=72, heritability_bits=1.2))
    print("Vincent 2024 protocells →", lifelikeness_score(network_cycles=12, persistence_hours=168, dissipation_rate=4.1))
