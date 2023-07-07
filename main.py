import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, tan, exp, arcsin, linspace, arange, sqrt, zeros, array, matrix, asmatrix
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, legend, grid, axis, tight_layout, grid, axis
import coattheory


def N(A, B, C, WL):
    return(A + B / (WL**2) + C / (WL**4))


def N_OHARA(A1, A2, A3, WL, B1, B2, B3):
    return((A1 * (WL**2)) / (WL**2 - B1) + (A2 * (WL**2)) / (WL**2 - B2) + (A3 * (WL**2)) / (WL**2 - B3))


t1start = 300
t1end = 1000
t1points = 700

WL = linspace(t1start, t1end, t1points)

matrixRP = np.zeros((t1points, t1points))
for i in range(t1points):
    n1 = N_OHARA(1.15150190, 1.18583612 * (10**(-1)), 1.26301359, WL[i], 1.05984130 * (10**(-2)), -1.18225190 * (10**(-2)), 1.29617662 * (10**2))
    n2 = N(2.266566, 20626.89, 6.29 * 10**9, WL[i])
    n3 = N(1.457341, 3417.464, 0, WL[i])
    n4 = N(2.266566, 20626.89, 6.29 * 10**9, WL[i])
    n5 = 1
    d2 = 57.42
    d3 = 93.6
    d4 = 57.42
    t = 0
    # print(WL[i])
    matrix1 = coattheory.matrixformat(n1, n2, n3, n4, n5, d2, d3, d4, WL, t)
    # print(matrix1[1])


plt.plot(WL, matrix1[2])
plt.show()
