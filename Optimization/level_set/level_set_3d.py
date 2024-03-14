import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw(f, x, y, c):
    # Generate grid points
    X, Y = np.meshgrid(x, y)
    
    # Compute function values
    Z = f(X, Y)
    
    # Plot 3D surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    
    # Plot level set
    ax.contour(X, Y, Z, levels=[c], colors='red')
    
    # Customize labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <c_level>")
        sys.exit(1)
    
    c = float(sys.argv[1])

    # Define your function here or import it from another module
    def example_function(x, y):
        return 2*x**3 + y**2

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    draw(example_function, x, y, c)
