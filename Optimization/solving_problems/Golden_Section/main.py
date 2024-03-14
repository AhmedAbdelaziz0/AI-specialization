import numpy as np
import matplotlib.pyplot as plt


def plot_function_with_shaded_area(
    f, x_domain, shaded_region_start, shaded_region_end, x_points, x_names
):
    # Generate x values
    x = np.linspace(x_domain[0], x_domain[1], 1000)

    # Generate y values
    y = f(x)
    # Create the plot
    plt.figure(figsize=(8, 6))

    # Plot the function
    plt.plot(x, y, "b", label="$f(x)$")

    # Shade the specified area under the curve
    plt.fill_between(
        x,
        y,
        where=[(val >= shaded_region_start and val <= shaded_region_end) for val in x],
        color="green",
        alpha=0.3,
    )

    # Plot perpendicular lines at x_points
    for i, x_point in enumerate(x_points):
        plt.axvline(x=x_point, linestyle="--", color="black")  # Draw perpendicular line
        plt.text(
            x_point, 0, x_names[i], verticalalignment="top", horizontalalignment="left"
        )  # Add text label

    # Evaluate f(x) at x_points and plot points
    y_points = f(np.array(x_points))
    plt.scatter(x_points, y_points, color="black", zorder=5)  # Plot points

    # Add labels and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of $f(x)$ with shaded area")
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()


def golden_section_method(objective_function, initial_interval, tolerance=1e-6):
    # Define the golden ratio
    a, b = initial_interval
    intervals = [{"a0": a, "b0": b}]
    values = []

    golden_ratio = (3 - 5**0.5) / 2  # Approximately 0.61803398875

    # Initialize the iteration counter
    iteration = 1

    # Iterate until convergence
    while b - a > tolerance:
        # Calculate the interior points c and d using the golden ratio
        c = a + golden_ratio * (b - a)
        d = a + (1 - golden_ratio) * (b - a)
        values.append([c, d])
        # Evaluate the objective function at the interior points
        fc = objective_function(c)
        fd = objective_function(d)

        # Update the interval based on the values of f(c) and f(d)
        items = list(intervals[-1].items())

        if fc < fd:
            b = d  # Discard the interval [c, b]
            intervals.append({items[0][0]: items[0][1], f"b{iteration}": b})
        else:
            a = c  # Discard the interval [a, d]
            intervals.append({f"a{iteration}": a, items[1][0]: items[1][1]})

        # Increment the iteration counter
        iteration += 1
    return intervals, values


class Plotter:
    def __init__(self, objective_function, initial_interval, intervals, inter_values):
        self.objective_function = objective_function
        self.initial_interval = initial_interval
        self.intervals = intervals
        self.inter_values = inter_values

    def plot(self):
        plot_function_with_shaded_area(
            self.objective_function, self.initial_interval, 0, 0, [], []
        )

        for i in range(len(self.intervals) - 1):
            interval_values = list(self.intervals[i].values())
            x_points = [
                *interval_values,
                self.inter_values[i][0],
                self.inter_values[i][1],
            ]
            shaded_region = [x_points[0], x_points[1]]

            interval_keys = list(self.intervals[i].keys())
            x_names = [*interval_keys, f"a{i+1}", f"b{i+1}"]

            for j in range(4):
                x_names[j] = x_names[j] + f"\n{x_points[j]:.2}"

            plot_function_with_shaded_area(
                self.objective_function,
                self.initial_interval,
                shaded_region[0],
                shaded_region[1],
                x_points,
                x_names,
            )

        x_points = list(self.intervals[-1].values())
        x_names = list(self.intervals[-1].keys())

        for i in range(2):
            x_names[i] = x_names[i] + f"\n{x_points[i]:.4}"

        plot_function_with_shaded_area(
            self.objective_function,
            self.initial_interval,
            x_points[0],
            x_points[1],
            x_points,
            x_names,
        )


class TableDisplay:
    def __init__(self, objective_function, intervals, initial_interval, inter_values):
        self.objective_function = objective_function
        self.intervals = intervals
        self.initial_interval = initial_interval
        self.inter_values = inter_values

    def display_tables(self):
        def display_table(data):
            plt.figure(
                figsize=(6, 4),
                dpi=250,
            )
            plt.axis("off")
            plt.table(
                cellText=data,
                loc="center",
                cellLoc="center",
                colLabels=None,
            )
            plt.show()

        data = [
            ["", "$a$", "$b$", "$f(a)$", "$f(b)$", "start interval", "end interval"],
            [
                "0",
                *self.initial_interval,
                "-",
                "-",
                self.initial_interval[0],
                self.initial_interval[1],
            ],
        ]
        # display_table(data)

        for i, _ in enumerate(self.inter_values):
            iteration = f"{i+1}"
            row = [*self.inter_values[i]]  # a, b
            row.append(self.objective_function(row[0]))  # fa
            row.append(self.objective_function(row[1]))  # fb
            for j in range(4):
                row[j] = f"{row[j]:.4}"
            interval = [f"{j:.4}" for j in self.intervals[i + 1].values()]
            data.append([iteration, *row, *interval])
        display_table(data)


def main():
    # Example usage:
    def objective_function(x):
        return x**2 - 4 * x + 4


    initial_interval = [0.0, 1.6]
    intervals, inter_values = golden_section_method(
        objective_function, initial_interval, 0.4
    )

    plotter = Plotter(objective_function, initial_interval, intervals, inter_values)
    plotter.plot()

    table_display = TableDisplay(
        objective_function, intervals, initial_interval, inter_values
    )
    table_display.display_tables()

if __name__ == '__main__':
    main()
