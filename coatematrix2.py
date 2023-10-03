import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, tan, exp, arcsin, linspace, arange, sqrt, zeros, array, matrix, asmatrix
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, legend, grid, axis, tight_layout, grid, axis


def matrixformat2(n1, n2, d2, WL, t):

    def matFAI(k0, n1z, d1):
        return matrix([[exp(1j * n1z * k0 * d1), 0], [0, exp(-1j * n1z * k0 * d1)]])

      # 媒質1の屈折率
      # 媒質2 "

    k0 = 2 * pi / WL
    t1 = (t / 180) * pi
    s1 = sin(t1)
    c1 = sqrt(1 - s1**2)
    s2 = (n1 / n2) * s1
    c2 = sqrt(1 - s2**2)

    n1z = n1 * c1
    n2z = n2 * c2

    matFAI2 = zeros((2, 2), dtype=complex)

    matFAI2 = matFAI(k0, n1z, d2)

    return(matFAI2)


# plot(WL,R,label="R")
