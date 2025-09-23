#Z-transform of the sequence x[n]=3^n u[n].
import sympy as sp

# Define variables
n, z = sp.symbols('n z')

# Define the sequence x[n] = 3^n * u[n]
x_n = 3**n   # since u[n] ensures n >= 0

# Compute the Z-transform: X(z) = Σ (3^n * z^(-n)), n = 0..∞
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Display result
print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(X_z, use_unicode=True)
