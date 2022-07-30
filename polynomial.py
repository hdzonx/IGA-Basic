'''Parametric construction of a 2nd order polynomial curve'''
# Nodal coordinates xi and yi
#xi = a0 + a1*t + a2*t**2
#yi = b0 + b1*t + b2*t**2
# For this example P0(-5,2) P1(3,5) P2(9,2) are the control points

import numpy as np
import matplotlib.pyplot as plt

coordinate_vector = [-5, 3, 9, 2, 5, 2]

# Natural coordinates csi1 = -1, csi2 = 0 and csi3 = 1
csi1 = -1
csi2 = 0
csi3 = 1

#Parametrix matrix
T = [[1, csi1,  csi1**2,  0,    0,       0],
     [1, csi2,  csi2**2,  0,    0,       0],
     [1, csi3,  csi3**2,  0,    0,       0],
     [0,  0,     0,       1,  csi1, csi1**2],
     [0,  0,     0,       1,  csi2, csi2**2],
     [0,  0,     0,       1,  csi3, csi3**2]]

#Invese of the parametrix matrix
#AX=B
#AA^-1X=BA^-1
#X=BA^-1
T_inverse = np.linalg.inv(T)

#Coeficients a's and b's calculation
Coeff = np.dot(T_inverse, coordinate_vector)
print(Coeff)

#Now, with the coefficients, we can construct the curve
#We will use the parametrix function
def parametrix(t):
    x = Coeff[0] + Coeff[1]*t + Coeff[2]*t**2
    y = Coeff[3] + Coeff[4]*t + Coeff[5]*t**2
    return x, y

for t in np.linspace(-10, 10, 100):
    x, y = parametrix(t)
    plt.plot(x, y, '.')
plt.show()