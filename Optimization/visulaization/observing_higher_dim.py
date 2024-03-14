import numpy as np
import matplotlib.pyplot as plt

def plot(X, Y, Z):
    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')

    # Customize labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Surface Plot')

    # Add a color bar
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Show plot
    plt.show()

# Create data
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)

while True:
    i = int(input("""Choose a function
              1) f(x, y) = x + y
              2) f(x, y) = x^2 + y
              3) f(x, y) = x^2 + y^2
              4) f(x, y) = x^2 - y^2
              5) f(x, y) = x^3 + y^3
              6) f(x, y) = sqrt(x^2 + y^2)
              7) f(x, y) = sin(x) + sin(y)
              8) f(x, y) = sin(x) - cos(y)
              0) exit
              """))
    if i == 1:
        plot(X, Y, X+Y)
    elif i == 2:
        plot(X, Y, X**2 + Y)
    elif i == 3:
        plot(X, Y, X**2 + Y**2)
    elif i == 4:
        plot(X, Y, X**2 - Y**2)
    elif i == 5:
        plot(X, Y, X**3 + Y**3)
    elif i == 6:
        plot(X, Y, np.sqrt(X**2 + Y**2))
    elif i == 7:
        plot(X, Y, np.sin(X) + np.sin(Y))
    elif i == 8:
        plot(X, Y, np.sin(X) - np.cos(Y))
    elif i == 0:
        break
    else:
        print("write valid option")
