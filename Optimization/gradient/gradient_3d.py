import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Define the function symbolically
f_sym = x**2 + y**2

# Compute the gradient symbolically
gradient_f_sym = sp.Matrix([f_sym.diff(x), f_sym.diff(y)])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate grid points for visualization
x_vals = np.linspace(-2, 2, 20)
y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Define functions for numerical evaluation
f = sp.lambdify((x, y), f_sym, 'numpy')
gradient_f = sp.lambdify((x, y), gradient_f_sym, 'numpy')

# Evaluate the function and gradient at each grid point
Z = f(X, Y)
dX, dY = gradient_f(X, Y)

# Plot the function surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=1)

# Plot the gradient as vectors
x_vals = np.linspace(-2, 2, 6)
y_vals = np.linspace(-2, 2, 6)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)
dX, dY = gradient_f(X, Y)
ax.quiver(X, Y, Z, dX, dY, 0, color='red', normalize=True, alpha=0.7)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('3D Plot with Gradient Vectors')
plt.show()
