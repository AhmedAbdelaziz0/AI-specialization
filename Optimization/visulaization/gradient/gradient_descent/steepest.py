import sympy as sp


def derivative_of_function(expression, variable, order=1):
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)

    if order == 1:
        derivative_expr = sp.diff(expr, x)
    elif order == 2:
        derivative_expr = sp.diff(expr, x, 2)
    else:
        raise ValueError(
            "Order must be 1 or 2 for first or second derivative, respectively.")

    return derivative_expr


def newton_method_optimization(expression, variable, initial_guess, iterations=1000, tolerance=1e-6):
    first_der = derivative_of_function(expression, variable)
    second_der = derivative_of_function(expression, variable, order=2)

    x = initial_guess
    for i in range(iterations):
        x_prev = x
        x = x - first_der.subs({variable: x}) / second_der.subs({variable: x})

        # Check if the difference between successive values of x is below the tolerance
        if abs(x - x_prev) < tolerance:
            break

    return x


def gradient_of_function(expression, variables):
    symbols = [sp.Symbol(var) for var in variables]
    expr = sp.sympify(expression)

    gradient_expr = [sp.diff(expr, var) for var in symbols]

    return gradient_expr


def steepest_descent_optimization(expression, variables, initial_values, iterations=1000, tolerance=1e-6):
    for iteration in range(iterations):
        # Calculate gradient at initial values
        gradient = gradient_of_function(expression, variables)
        gradient_x0 = [grad.subs(initial_values) for grad in gradient]

        # Check if gradient is close to zero (convergence achieved)
        if all(abs(grad) < tolerance for grad in gradient_x0):
            break

        # Define alpha as a symbolic variable
        alpha = sp.Symbol("alpha")

        # Define phi expression for the line search
        phi_expression = {
            var: initial_values[var] - alpha * grad for var, grad in zip(variables, gradient_x0)}
        phi = sp.sympify(expression).subs(phi_expression)

        # Use Newton's method to find the optimal alpha
        alpha_value = newton_method_optimization(str(phi), "alpha", 1)

        # Update values using steepest descent formula
        new_values = {var: initial_values[var] - alpha_value *
                      grad for var, grad in zip(variables, gradient_x0)}

        print(new_values)
        # Update initial_values for next iteration
        initial_values = new_values

    return initial_values


# Example usage:
if __name__ == '__main__':
    function_expression = "0.25 * x ** 4 + y ** 2 + x ** 2 * y ** 2 - 2 * x - 2 * y + 3"
    variables = ["x", "y"]
    initial_values = {"x": 4, "y": 4}  # Adjusted initial values

    optimized_values = steepest_descent_optimization(
        function_expression, variables, initial_values)
    print("Optimized values:", optimized_values)
