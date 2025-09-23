#	Using Python, compute the Z-transform of the sequence x[n]=cos⁡(wn)u[n]
import sympy as sp

# Define symbols
n, z, w = sp.symbols('n z w', real=True)

# Define sequence: x[n] = cos(w*n) * u[n], so only n >= 0
x_n = sp.cos(w*n)

# Compute Z-transform: X(z) = Σ cos(w*n) * z^(-n), n=0..∞
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Simplify the result
X_z_simplified = sp.simplify(X_z)

# Display result
print("Z-transform of x[n] = cos(w*n) u[n]:")
sp.pprint(X_z_simplified, use_unicode=True)
