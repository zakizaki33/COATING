import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, tan, exp, arcsin, linspace, arange, sqrt, zeros, array, matrix, asmatrix
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, legend, grid, axis, tight_layout, grid, axis


def matrixformat1(n1, n2, t):
    def mMATs(n1z, n2z):
        return(1 / (2 * n1z)) * matrix([[n1z + n2z, n1z - n2z], [n1z - n2z, n1z + n2z]])

    def mMATp(n1z, n2z, n1, n2):
        return(1 / (2 * n1 * n2 * n1z)) *\
            matrix([[n1**2 * n2z + n2**2 * n1z, n1**2 * n2z - n2**2 * n1z], [n1**2 * n2z - n2**2 * n1z, n1**2 * n2z + n2**2 * n1z]])

      # 媒質1の屈折率
      # 媒質2 "

    t1 = (t / 180) * pi  # 入射角（rad）
    s1 = sin(t1)
    c1 = cos(t1)
    s2 = (n1 / n2) * s1  # 境界条件
    c2 = sqrt(1 - s2**2)
    # S2 C2屈折ベクトル

    n1z = n1 * c1
    n2z = n2 * c2

    mMats21 = zeros((2, 2), dtype=complex)
    mMatp21 = zeros((2, 2), dtype=complex)

    matTs = zeros((2, 2), dtype=complex)
    matTp = zeros((2, 2), dtype=complex)

    mMats21 = mMATs(n1z, n2z)

    mMatp21 = mMATp(n1z, n2z, n1, n2)

    matTs = mMats21

    matTp = mMatp21

    return(matTs, matTp)


# plot(WL,R,label="R")
