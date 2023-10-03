import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, tan, exp, arcsin, linspace, arange, sqrt, zeros, array, matrix, asmatrix
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, legend, grid, axis, tight_layout, grid, axis
import coatematrix1
import coatematrix2


def matrixformatX(n1, n2, d2, WL, t, n):

  # 媒質1の屈折率
  # 媒質2 "

    mMats21 = coatematrix1.matrixformat1(n1, n2, t)[0]

    mMatp21 = coatematrix1.matrixformat1(n1, n2, t)[1]

    matFAI2 = coatematrix2.matrixformat2(n1, n2, d2, WL, t)

    matTs = mMats21 @ matFAI2
    matTs = np.linalg.matrix_power(matTs, n)  # 行列をn剰（同じ膜をn枚はる）

    matTp = mMatp21 @ matFAI2
    matTp = np.linalg.matrix_power(matTp, n)  # 行列をn剰（同じ膜をn枚はる）

    return(matTs, matTp)


# plot(WL,R,label="R")
