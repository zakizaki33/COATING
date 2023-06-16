import matplotlib.pyplot as plt
from numpy import zeros, linspace, full, exp, sin, cos, array, nan, eye
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


# 位相の計算
def matFAI(n1z, d1, k0):
    return matrix([[exp(1j * n1z * k0 * d1), 0],
                   [0, exp(-1j * n1z * k0 * d1)]])


# 波長の設定
WL_start = 300
WL_end = 999
WL_points = WL_end - WL_start + 1
# WL = 500
WL = linspace(WL_start, WL_end, WL_points)
k0 = 2 * pi / WL

# n1空気、n2,n3,n4 膜、n5基材

layer_num = 24 + 2

# この入力形式で屈折率を入れていく
index = array([full(WL_points, 1.0),
               # full(WL_points, 1.38),  # 1.38
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.46),  # 2.10
               full(WL_points, 2.30),  # 1.63
               full(WL_points, 1.52)])
print("index.shape is", index.shape)

# distance は手動で入れざる負えない
distance = array([nan,
                  # 50 / 1.38,  # 99.64
                  # 50 / 1.38,  # 130.95
                  # 37.5 / 1.38,  # 84.35
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  137.5 / 1.46,
                  137.5 / 2.30,
                  nan])

# t1Deg = linspace(t1start, t1end, t1points)
t1Deg = 0
t1 = t1Deg / 180 * pi


s_array = zeros((layer_num, WL_points))  # arrayの形を合わせる
c_array = zeros((layer_num, WL_points))  # arrayの形を合わせる


for i in range(layer_num):
    if (i == 0):
        s_array[i] = index[i] * sin(t1)
        c_array[i] = index[i] * cos(t1)

    s_array[i] = s_array[0] / index[i]
    c_array[i] = sqrt(1 - s_array[i] ** 2)


nz_array = zeros((layer_num, WL_points))


for i in range(0, layer_num):
    nz_array[i] = index[i] * c_array[i]

# S偏光
mMats_array = zeros((layer_num, WL_points, 2, 2), dtype="complex")  # 4次元配列()

# P偏光
mMatp_array = zeros((layer_num, WL_points, 2, 2), dtype="complex")  # 4次元配列()

# 位相
matFAI_array = zeros((layer_num, WL_points, 2, 2), dtype="complex")  # 4次元配列()
print("matFAI_array.shape is", matFAI_array.shape)
# 最初の要素だけは単位行列にしておく
matFAI_array[0] = eye(2)

matTs = zeros((WL_points, 2, 2), dtype="complex")
matTp = zeros((WL_points, 2, 2), dtype="complex")
rs = zeros(WL_points, dtype="complex")
rp = zeros(WL_points, dtype="complex")
RsAbs = zeros(WL_points)
RpAbs = zeros(WL_points)

for i in range(WL_points):

    for j in range(0, layer_num - 1):
        mMats_array[j][i] = mMATs(nz_array[j + 1][i], nz_array[j][i])

    for j in range(0, layer_num - 1):
        mMatp_array[j][i] = mMATp(nz_array[j + 1][i], nz_array[j][i],
                                  index[j + 1][i], index[j][i])

    for j in range(1, layer_num - 1):
        matFAI_array[j][i] = matFAI(nz_array[j][i], distance[j], k0[i])

    matTs[i] = eye(2)  # 一旦単位行列に
    for j in range(0, layer_num - 1):
        matTs[i] = mMats_array[j][i] @ matFAI_array[j][i] @ matTs[i]

    matTp[i] = eye(2)  # 一旦単位行列に
    for j in range(0, layer_num - 1):
        matTp[i] = mMatp_array[j][i] @ matFAI_array[j][i] @ matTp[i]

    rs[i] = -matTs[i, 1, 0] / matTs[i, 1, 1]
    rp[i] = -matTp[i, 1, 0] / matTp[i, 1, 1]
    RsAbs[i] = abs(rs[i] ** 2)
    RpAbs[i] = abs(rp[i] ** 2)

plt.figure(figsize=(8, 6))
plot(WL, RpAbs, label=r"$R_{15}^{\rm{p}}$", linewidth=3.0,
     linestyle='dashed')
plot(WL, RsAbs, label=r"$R_{15}^{\rm{s}}$", linewidth=3.0,
     linestyle='solid')

xlabel(r"$wave length$[nm]", fontsize=20)
ylabel("Reflectivity", fontsize=20)
title("Reflectivity", fontsize=18)
legend(fontsize=20, loc='lower right')
grid(True)

axis([300, 999, 0, 1.2])

tight_layout()
show()
