# Biogenesis Convergence Observatory

**Turning the origin of life into a measurable, convergent engineering challenge.**

> “We don’t need to know the historical pathway. We need to know how close we can get in the lab — today.”

Ignited: November 18, 2025  
Captain: @AnantaV4

## Lifelikeness Score v0.1 (copy-paste and run)
```python
import numpy as np

def lifelikeness_score(network_cycles=1, persistence_hours=0, dissipation_rate=0, heritability_bits=0):
    N = min(np.log10(max(network_cycles, 1)) / 5, 1.0)   # Autocatalysis
    C = min(persistence_hours / 500.0, 1.0)              # Compartment persistence
    E = min(dissipation_rate / 10.0, 1.0)                # Energy transduction
    H = min(heritability_bits / 8.0, 1.0)                # Heritable variation
    return round(N + C + E + H, 3)

# Real 2020–2025 systems
print("Szostak vesicles →", lifelikeness_score(persistence_hours=72, heritability_bits=1.2))          # ~0.25
print("Vincent protocells →", lifelikeness_score(network_cycles=12, persistence_hours=168, dissipation_rate=4.1))  # ~1.93
