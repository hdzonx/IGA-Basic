""" The Bézier curve represent a important type of curve used in
computer graphics. It is a curve that is defined by a set of points.
The nth-order Bézier curve is given by the following formula:
x = ∑Bi,n(ξ) Pxi
y = ∑Bi,n(ξ) Pyi
-1 ≤ ξ ≤ 1
Bi,n(ξ) is the Bernstein polynomial of order n.
Pxi and Pyi are the control points.
Reference book: Gan, B. (2018). "An Isogeometric aprroach to beam structures." Springer.
"""

import numpy as np
import matplotlib.pyplot as plt
from lin_algebra import Matrix


def factorial(n):
    """Factorial of n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def Bernstein(n, i, t):
    """Bernstein polynomial of order n and i in the range -1 ≤ ξ ≤ 1.
    In the function, n is the order of the Bernstein polynomial, i is the
    index. t == ξ and -1 ≤ ξ ≤ 1."""
    return (factorial(n) / (factorial(i) * factorial(n - i)))*(((1+t)/2)**i)*((1-t)/2)**(n-i)


def Bezier_curve(n, P):
    """Bernstein curve of order n and control points P.
    In the function, n is the order of the Bernstein curve, P is the list of
    control points.
    """
    x = 0
    y = 0
    dt = 1/50
    # Array of t values -1 ≤ ξ ≤ 1, with dt steps.
    t_array = np.arange(-1, 1, dt)
    for i in range(n+1):
        for t in t_array:
            x += Bernstein(n, i, t)*P[i][0]
            y += Bernstein(n, i, t)*P[i][1]
    return x, y


def get_Bernstein_function_only(n, i):
    """get only Bernstein function of order n in 
    the range -1 ≤ ξ ≤ 1, for index i."""
    dt = 1/50
    t_array = np.arange(-1, 1, dt)
    y_arr = []
    y = 0

    for t in t_array:
        y = Bernstein(n, i, t)
        y_arr.append(y)
    return t_array, y_arr


def plot_Bernstein_curves(n):
    """plot Bernstein curve of polinominal order n and index from zero to n. 
    in the range -1 ≤ ξ ≤ 1."""
    i = n
    for j in range(i + 1):
        t_array, y_arraY = get_Bernstein_function_only(n, j)
        plt.plot(t_array, y_arraY, label = "i = " + str(j))
    #Plotting the Bernstein curve    
    plt.title('Bernstein curve for polinomial order n = ' + str(n))
    plt.legend()
    plt.xlabel('ξ')
    plt.ylabel('B_{i,n}(ξ)')
    plt.show()


def Matrix_of_Bernstein_functions(n, t):
    """Matrix of Bernstein functions of order n in the range -1 ≤ ξ ≤ 1."""
    matrix = Matrix.Matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            matrix.data[i][j] = Bernstein(n, j, t[i])
    return matrix



#Call the function to plot the Bernstein curves
polinomial_Order = 2
Control_Points = [[-5, 2], [3, 5], [9, 2]] #Control points matrix wich x= first column and y = second column


plot_Bernstein_curves(polinomial_Order)

t = [-1, 0, 1]
matrix1 = Matrix_of_Bernstein_functions(polinomial_Order, t)

print(matrix1)

