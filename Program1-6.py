import matplotlib.pyplot as plt
from numpy import zeros, linspace, exp, sin, cos
from scipy import pi, matrix
from numpy.lib.scimath import sqrt
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, legend,
                               grid, axis, tight_layout)


# S偏光の境界条件
def mMATs(n1z, n2z):
    return (1 / (2 * n1z)) * matrix([[n1z + n2z, n1z - n2z],
                                     [n1z - n2z, n1z + n2z]])


# p偏光の境界条件
def mMATp(n1z, n2z, n1, n2):
    return (1 / (2 * n1 * n2 * n1z)) * \
        matrix([[n1 ** 2 * n2z + n2 ** 2 * n1z, n1 ** 2 * n2z - n2 ** 2 * n1z],
                [n1 ** 2 * n2z - n2 ** 2 * n1z, n1 ** 2 * n2z + n2 ** 2 * n1z]
                ])


def matFAI(n1z, d1, k0):
    return matrix([[exp(1j * n1z * k0 * d1), 0],
                   [0, exp(-1j * n1z * k0 * d1)]])


n1 = 1.0
n2 = 1.5
n3 = 1.0

ep1 = n1 ** 2
ep2 = n2 ** 2
ep3 = n3 ** 2

d2 = 100
WL = 500
k0 = 2 * pi / WL

t1start = 0
t1end = 89  # 90まで入れるとゼロ割が発生してしまう
t1points = 90

t1Deg = linspace(t1start, t1end, t1points)
t1 = t1Deg / 180 * pi
# t2 = arcsin((n1 / n2) * sin(t1))

s1 = sin(t1)  # sin(t1)
c1 = cos(t1)  # cos(t1)
s2 = n1 / n2 * s1  # sin(t2)
c2 = sqrt(1 - s2**2)  # cos(t2)
s3 = n1 / n3 * s1  # sin(t2)
c3 = sqrt(1 - s3**2)  # cos(t2)

n1z = n1 * c1
n2z = n2 * c2
n3z = n3 * c3

# 配列の初期化
mMats21 = zeros((t1points, 2, 2), dtype="complex")  # 3次元配列になっている
mMats32 = zeros((t1points, 2, 2), dtype="complex")
mMatp21 = zeros((t1points, 2, 2), dtype="complex")  # 3次元配列になっている
mMatp32 = zeros((t1points, 2, 2), dtype="complex")
matFAI2 = zeros((t1points, 2, 2), dtype="complex")
matTs = zeros((t1points, 2, 2), dtype="complex")
matTp = zeros((t1points, 2, 2), dtype="complex")
rs = zeros(t1points, dtype="complex")
rp = zeros(t1points, dtype="complex")
ts = zeros(t1points, dtype="complex")
tp = zeros(t1points, dtype="complex")


for i in range(t1points):
    mMats21[i] = mMATs(n2z[i], n1z[i])
    mMats32[i] = mMATs(n3z[i], n2z[i])
    mMatp21[i] = mMATp(n2z[i], n1z[i], n2, n1)
    mMatp32[i] = mMATp(n3z[i], n2z[i], n3, n2)

    matFAI2[i] = matFAI(n2z[i], d2, k0)

    matTs[i] = mMats32[i] @ matFAI2[i] @ mMats21[i]
    matTp[i] = mMatp32[i] @ matFAI2[i] @ mMatp21[i]

    rs[i] = -matTs[i, 1, 0] / matTs[i, 1, 1]
    rp[i] = -matTp[i, 1, 0] / matTp[i, 1, 1]
    ts[i] = matTs[i, 0, 0] - matTs[i, 0, 1] * matTs[i, 1, 0] / matTs[i, 1, 1]
    tp[i] = matTp[i, 0, 0] - matTp[i, 0, 1] * matTp[i, 1, 0] / matTp[i, 1, 1]
    

RsAbs = abs(rs ** 2)
RpAbs = abs(rp ** 2)

plt.figure(figsize=(8, 6))
plot(t1Deg, RpAbs, label=r"$R_{13}^{\rm{p}}$", linewidth=3.0,
     linestyle='dashed')
plot(t1Deg, RsAbs, label=r"$R_{13}^{\rm{s}}$", linewidth=3.0,
     linestyle='solid')

xlabel(r"$\theta_1$(deg.)", fontsize=20)
ylabel("Reflectivity", fontsize=20)
title("Reflectivity", fontsize=18)
legend(fontsize=20, loc='lower right')
grid(True)

axis([0.0, 90, 0, 1.1])

tight_layout()
show()
