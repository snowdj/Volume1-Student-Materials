# newtons_method.py
"""Volume 1: Newton's Method.
<Name>
<Class>
<Date>
"""


# Problems 1, 3, and 5
def newton(f, x0, Df, tol=1e-5, maxiters=15, alpha=1.):
    """Use Newton's method to approximate a root of the function f.

    Parameters:
        f (function): a function from R^n to R^n (assume n=1 until Problem 5).
        x0 (float or ndarray): The initial guess for the root of f.
        Df (function): The derivative of f, a function from R^n to R^(nxn).
        tol (float): Convergence tolerance. The function should returns when
            the difference between successive approximations is less than tol.
        maxiters (int): The maximum number of iterations to compute.
        alpha (float): Backtracking scalar (Problem 3).

    Returns:
        (float or ndarray): The approximation for a root of f.
        (bool): Whether or not Newton's method converged.
        (int): The number of iterations computed.
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2(N1, N2, P1, P2):
    """Use Newton's method to solve for the constant r that satisfies

                P1[(1+r)**N1 - 1] = P2[1 - (1+r)**(-N2)].

    Use r_0 = 0.1 for the initial guess.

    Parameters:
        P1 (float): Amount of money deposited into account at the beginning of
            years 1, 2, ..., N1.
        P2 (float): Amount of money withdrawn at the beginning of years N1+1,
            N1+2, ..., N1+N2.
        N1 (int): Number of years money is deposited.
        N2 (int): Number of years money is withdrawn.

    Returns:
        (float): the value of r that satisfies the equation.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 4
def optimal_alpha(f, x0, Df, tol=1e-5, maxiters=15):
    """Run Newton's method for various values of alpha in (0,1].
    Plot the alpha value against the number of iterations until convergence.

    Parameters:
        f (function): a function from R^n to R^n (assume n=1 until Problem 5).
        x0 (float or ndarray): The initial guess for the root of f.
        Df (function): The derivative of f, a function from R^n to R^(nxn).
        tol (float): Convergence tolerance. The function should returns when
            the difference between successive approximations is less than tol.
        maxiters (int): The maximum number of iterations to compute.

    Returns:
        (float): a value for alpha that results in the lowest number of
            iterations.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 6
def prob6():
    """Consider the following Bioremediation system.

                              5xy − x(1 + y) = 0
                        −xy + (1 − y)(1 + y) = 0

    Find an initial point such that Newton’s method converges to either
    (0,1) or (0,−1) with alpha = 1, and to (3.75, .25) with alpha = 0.55.
    Return the intial point as a 1-D NumPy array with 2 entries.
    """
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def plot_basins(f, Df, roots, domain, res=1000, iters=15):
    """Plot the basins of attraction of f on the complex plane.

    Parameters:
        f (function): A function from C to C.
        Df (function): The derivative of f, a function from C to C.
        roots (ndarray): A 1-D array of the roots of f.
        domain ([r_min, r_max, i_min, i_max]): A list of scalars that define
            the window limits and grid domain for the plot.
        res (int): A scalar that determines the resolution of the plot.
            The visualized grid has shape (res, res).
        iters (int): The exact number of times to iterate Newton's method.
    """
    raise NotImplementedError("Problem 7 Incomplete")
