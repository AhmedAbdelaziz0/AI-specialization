import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Define the function symbolically
f_sym = 2*x**3 + y**2

# Compute the gradient of the function symbolically
gradient_f_sym = sp.Matrix([f_sym.diff(var) for var in (x, y)])

# Convert symbolic expressions to lambdified functions for numerical evaluation
f = sp.lambdify((x, y), f_sym, 'numpy')
gradient_f = sp.lambdify((x, y), gradient_f_sym, 'numpy')

# Generate grid points for visualization
x_vals = np.linspace(-2, 2, 100)
y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Evaluate the function and gradient at each grid point
Z = f(X, Y)
dZ = gradient_f(X, Y)

# Extract components of the gradient and remove extra dimension
dX, dY = np.squeeze(dZ[0]), np.squeeze(dZ[1])

# Plot the function
plt.figure(figsize=(10, 6))
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label='Function Value')

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
