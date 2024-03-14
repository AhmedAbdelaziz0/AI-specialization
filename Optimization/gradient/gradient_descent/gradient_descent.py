import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp


def gradient_descent(f, grad_f, x0, alpha, max_iter):
    x = x0
    x_history = [x]
    for _ in range(max_iter):
        grad = grad_f(*x)
        x = x - alpha * np.array(grad).astype(float)
        x_history.append(x)
    return x_history


def visualize_optimization(f, x_history):
    x_history = np.array(x_history)
    x_range = np.linspace(min(x_history[:, 0]), max(x_history[:, 0]), 100)
    y_range = np.linspace(min(x_history[:, 1]), max(x_history[:, 1]), 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.scatter(x_history[:, 0], x_history[:, 1], f(x_history[:, 0], x_history[:, 1]), c='r',
               marker='o', linewidths=2)

    # Plot lines connecting consecutive points
    for i in range(len(x_history) - 1):
        x1, y1 = x_history[i]
        x2, y2 = x_history[i + 1]
        ax.plot([x1, x2], [y1, y2], [f(x1, y1), f(x2, y2)],
                color='b', linestyle='-', linewidth=2)

    plt.show()


# Define symbolic variables
x, y = sp.symbols('x y')

# Example objective function: f(x, y) = x^2 + y^2
f_symbolic =  0.25 * x**4 + y**2 * x**2 + y**2 - 2 * x - 2 * y + 3

# Gradient of the objective function: ∇f(x, y) = [2x, 2y]
grad_f_symbolic = [sp.diff(f_symbolic, x), sp.diff(f_symbolic, y)]

# Convert symbolic functions to lambdified functions for numerical computation
f = sp.lambdify((x, y), f_symbolic, 'numpy')
grad_f = sp.lambdify((x, y), grad_f_symbolic, 'numpy')

# Initial guess and hyperparameters
x0 = [1, 0.5]
alpha = 0.2
max_iter = 5

# Perform gradient descent
x_history = gradient_descent(f, grad_f, x0, alpha, max_iter)
print(x_history)

# Visualize optimization process
visualize_optimization(f, x_history)
