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
from xml.sax.saxutils import prepare_input_source
import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    """Factorial of n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def Bernstein(n, i, t):
    """Bernstein polynomial of order n and i in the range -1 ≤ ξ ≤ 1.
    In the function, n is the order of the Bernstein polynomial, i is the
    index. t == ξ."""
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


#n = 2
#dt = 1/50
#t_array = np.arange(-1, 1, dt)
#y_arr = []
#y = 0


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


def plot_Bernstein_curves(n, i):
    """plot Bernstein curve of order n and index i 
    in the range -1 ≤ ξ ≤ 1."""
    for j in range(i + 1):
        t_array, y_arraY = get_Bernstein_function_only(n, j)
        plt.plot(t_array, y_arraY, label = "i = " + str(j))
    #Plotting the Bernstein curve    
    plt.title('Bernstein curve for n = ' + str(n))
    plt.legend()
    plt.xlabel('ξ')
    plt.ylabel('B_{i,n}(ξ)')
    plt.show()


#Call the function to plot the Bernstein curves
plot_Bernstein_curves(4, 4)

