import sympy as sp

def derivative_of_function(expression, variable, order=1):
    """
    Calculate the derivative of a function with respect to a given variable using SymPy.

    Args:
    expression (str): The mathematical expression of the function.
    variable (str): The variable with respect to which the derivative is calculated.
    order (int): The order of the derivative. Default is 1 (first derivative).

    Returns:
    str: The derivative of the function.
    """
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)
    
    if order == 1:
        derivative_expr = sp.diff(expr, x)
    elif order == 2:
        derivative_expr = sp.diff(expr, x, 2)
    else:
        raise ValueError("Order must be 1 or 2 for first or second derivative, respectively.")
        
    return derivative_expr

def newton_method_optimization(expression, variable, initial_guess, iterations=10):
    """
    Perform optimization using Newton's method.

    Args:
    expression (str): The mathematical expression of the function.
    variable (str): The variable with respect to which the derivative is calculated.
    initial_guess (float): Initial guess for the root.
    iterations (int): Number of iterations. Default is 10.

    Returns:
    float: The optimized value.
    """
    first_der = derivative_of_function(expression, variable)
    second_der = derivative_of_function(expression, variable, order=2)
    
    x = initial_guess
    for _ in range(iterations):
        x = x - first_der.subs(variable, x) / second_der.subs(variable, x)
    return x


if __name__ == "__main__":
    # Example usage:
    function_expression = "1/4 * x ** 4 - 4/3 * x**3 + x**2 - x + 5"  # Example function: f(x) = x^3 + 2x^2 + x
    variable = "x"
    initial_guess = 1.0
    optimized_value = newton_method_optimization(function_expression, variable, initial_guess, 100)
    print("Optimized value:", optimized_value)
