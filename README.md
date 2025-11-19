# # Biogenesis Convergence Observatory

**A convergent multi-modal framework for experimental origins-of-life research**  
Turning the origin of life from a historical mystery into a laboratory engineering problem.

> “We don’t need to agree on the pathway. We just need to agree on how to measure how close we are.”

## Lifelikeness Score v0.1 (run it right now)
```python
import numpy as np

def lifelikeness_score(network_cycles=1, persistence_hours=0, dissipation_rate=0, heritability_bits=0):
    N = min(np.log10(max(network_cycles, 1)) / 5, 1.0)   # Autocatalysis
    C = min(persistence_hours / 500.0, 1.0)              # Compartment
    E = min(dissipation_rate / 10.0, 1.0)                # Energy
    H = min(heritability_bits / 8.0, 1.0)                # Information
    return round(N + C + E + H, 3)

# Real published systems (2025 values)
print("Szostak vesicles →", lifelikeness_score(persistence_hours=72, heritability_bits=1.2))      # ~0.25
print("Vincent protocells →", lifelikeness_score(network_cycles=12, persistence_hours=168, dissipation_rate=4.1))  # ~1.9
