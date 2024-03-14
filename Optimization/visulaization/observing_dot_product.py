import numpy as np
import matplotlib.pyplot as plt

def visualize_3d_vectors(vector1, vector2):
    # Calculate the dot product
    dot_product = np.dot(vector1, vector2)

    # Create a figure and a 3D axis
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the vectors
    origin = np.zeros(3)
    ax.quiver(*origin, *vector1, color='r', label='Vector 1')
    ax.quiver(*origin, *vector2, color='b', label='Vector 2')

    # Set plot limits
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Add grid and labels
    ax.grid(True)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Dot Product = {}'.format(dot_product))

    # Add legend
    ax.legend()

    # Show plot
    plt.show()

def to_unit_vector(x):
    return x / np.linalg.norm(x)

def to_unit(vectors):
    for i in range(len(vectors)):
        vectors[i][0] = to_unit_vector(vectors[i][0])
        vectors[i][1] = to_unit_vector(vectors[i][1])
    return vectors

# Examples
examples = [
    [np.array([2, 3, 1]), np.array([-1, 4, 2])],  # Example 1
    [np.array([2, 3, 1]), np.array([4, 6, 2])],   # Example 2
    [np.array([2, 3, 1]), np.array([-2, -3, -1])],  # Example 3
    [np.array([1, 0, 0]), np.array([0, 1, 0])],    # Example 4
    [np.array([2, 3, 1]), np.array([1, 2, 2])],    # Example 5
    [np.array([2, 3, 1]), np.array([-1, -2, -2])]  # Example 6
]

examples = to_unit(examples)

# Visualize examples
for i, (vector1, vector2) in enumerate(examples, start=1):
    print(f"Example {i}:")
    visualize_3d_vectors(vector1, vector2)
