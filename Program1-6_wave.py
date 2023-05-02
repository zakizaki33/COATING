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

layer_num = 5
"""
n1 = full(WL_points, 1.0)
n2 = full(WL_points, 1.38)
n3 = full(WL_points, 2.10)
n4 = full(WL_points, 1.63)
n5 = full(WL_points, 1.52)
index = array([n1, n2, n3, n4, n5])  # 層数、波長の2Dマトリックス
"""
# この入力形式で屈折率を入れていく
index = array([full(WL_points, 1.0),
               full(WL_points, 1.38),
               full(WL_points, 2.10),
               full(WL_points, 1.63),
               full(WL_points, 1.52)])
print("index.shape is", index.shape)

"""
ep1 = n1 ** 2
ep2 = n2 ** 2
ep3 = n3 ** 2
ep4 = n4 ** 2
ep5 = n5 ** 2

ep = index ** 2
print("ep.shape is", ep.shape)
"""

""""
d2 = 99.64
d3 = 130.95
d4 = 84.35
distance = zeros(layer_num)
distance[1] = d2
distance[2] = d3
distance[3] = d4
"""
# distance は手動で入れざる負えない
distance = array([nan,
                  99.64,
                  130.95,
                  84.35,
                  nan])

# t1Deg = linspace(t1start, t1end, t1points)
t1Deg = 35
t1 = t1Deg / 180 * pi

"""
s1 = n1 * sin(t1)  # sin(t1)
c1 = n1 * cos(t1)  # cos(t1)
s2 = s1 / n2   # sin(t2)
c2 = sqrt(1 - s2**2)  # cos(t2)
s3 = s1 / n3   # sin(t3)
c3 = sqrt(1 - s3**2)  # cos(t3)
s4 = s1 / n4
c4 = sqrt(1 - s4**2)
s5 = s1 / n5
c5 = sqrt(1 - s5**2)
"""

s_array = zeros((layer_num, WL_points))  # arrayの形を合わせる
c_array = zeros((layer_num, WL_points))  # arrayの形を合わせる

"""
s_array[0] = index[0] * sin(t1)
c_array[0] = index[0] * cos(t1)
s_array[1] = s_array[0] / index[1]
c_array[1] = sqrt(1 - s_array[1] ** 2)
s_array[2] = s_array[0] / index[2]
c_array[2] = sqrt(1 - s_array[2] ** 2)
s_array[3] = s_array[0] / index[3]
c_array[3] = sqrt(1 - s_array[3] ** 2)
s_array[4] = s_array[0] / index[4]
c_array[4] = sqrt(1 - s_array[4] ** 2)
"""

for i in range(layer_num):
    if (i == 0):
        s_array[i] = index[i] * sin(t1)
        c_array[i] = index[i] * cos(t1)
    
    s_array[i] = s_array[0] / index[i]
    c_array[i] = sqrt(1 - s_array[i] ** 2)


# n1z = n1 * c1
# n2z = n2 * c2
# n3z = n3 * c3
# n4z = n4 * c4
# n5z = n5 * c5
# print("n1z.shape is", n1z.shape)
nz_array = zeros((layer_num, WL_points))
# nz_array[0] = index[0] * c_array[0]
# nz_array[1] = index[1] * c_array[1]
# nz_array[2] = index[2] * c_array[2]
# nz_array[3] = index[3] * c_array[3]
# nz_array[4] = index[4] * c_array[4]

for i in range(0, layer_num):
    nz_array[i] = index[i] * c_array[i]

# S偏光
# mMats21 = zeros((WL_points, 2, 2), dtype="complex")  # 3次元配列になっている
# mMats32 = zeros((WL_points, 2, 2), dtype="complex")
# mMats43 = zeros((WL_points, 2, 2), dtype="complex")
# mMats54 = zeros((WL_points, 2, 2), dtype="complex")
mMats_array = zeros((layer_num, WL_points, 2, 2), dtype="complex")  # 4次元配列()

# P偏光
# mMatp21 = zeros((WL_points, 2, 2), dtype="complex")
# mMatp32 = zeros((WL_points, 2, 2), dtype="complex")
# mMatp43 = zeros((WL_points, 2, 2), dtype="complex")
# mMatp54 = zeros((WL_points, 2, 2), dtype="complex")
mMatp_array = zeros((layer_num, WL_points, 2, 2), dtype="complex")  # 4次元配列()


# 位相
# matFAI2 = zeros((WL_points, 2, 2), dtype="complex")
# matFAI3 = zeros((WL_points, 2, 2), dtype="complex")
# matFAI4 = zeros((WL_points, 2, 2), dtype="complex")
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
    # mMats21[i] = mMATs(n2z[i], n1z[i])
    # mMats32[i] = mMATs(n3z[i], n2z[i])
    # mMats43[i] = mMATs(n4z[i], n3z[i])
    # mMats54[i] = mMATs(n5z[i], n4z[i])
    # mMats21[i] = mMATs(nz_array[1][i], nz_array[0][i])
    # mMats32[i] = mMATs(nz_array[2][i], nz_array[1][i])
    # mMats43[i] = mMATs(nz_array[3][i], nz_array[2][i])
    # mMats54[i] = mMATs(nz_array[4][i], nz_array[3][i])
    # mMats_array[0][i] = mMATs(nz_array[1][i], nz_array[0][i])
    # mMats_array[1][i] = mMATs(nz_array[2][i], nz_array[1][i])
    # mMats_array[2][i] = mMATs(nz_array[3][i], nz_array[2][i])
    # mMats_array[3][i] = mMATs(nz_array[4][i], nz_array[3][i])
    for j in range(0, layer_num - 1):
        mMats_array[j][i] = mMATs(nz_array[j + 1][i], nz_array[j][i])

    # mMatp21[i] = mMATp(n2z[i], n1z[i], n2[i], n1[i])
    # mMatp32[i] = mMATp(n3z[i], n2z[i], n3[i], n2[i])
    # mMatp43[i] = mMATp(n4z[i], n3z[i], n4[i], n3[i])
    # mMatp54[i] = mMATp(n5z[i], n4z[i], n5[i], n4[i])
    # mMatp_array[0][i] = mMATp(nz_array[1][i], nz_array[0][i], n2[i], n1[i])
    # mMatp_array[1][i] = mMATp(nz_array[2][i], nz_array[1][i], n3[i], n2[i])
    # mMatp_array[2][i] = mMATp(nz_array[3][i], nz_array[2][i], n4[i], n3[i])
    # mMatp_array[3][i] = mMATp(nz_array[4][i], nz_array[3][i], n5[i], n4[i])
    """
    mMatp_array[0][i] = mMATp(nz_array[1][i], nz_array[0][i],
                              index[1][i], index[0][i])
    mMatp_array[1][i] = mMATp(nz_array[2][i], nz_array[1][i],
                              index[2][i], index[1][i])
    mMatp_array[2][i] = mMATp(nz_array[3][i], nz_array[2][i],
                              index[3][i], index[2][i])
    mMatp_array[3][i] = mMATp(nz_array[4][i], nz_array[3][i],
                              index[4][i], index[3][i])
    """
    for j in range(0, layer_num - 1):
        mMatp_array[j][i] = mMATp(nz_array[j + 1][i], nz_array[j][i],
                                  index[j + 1][i], index[j][i])

    """
    matFAI2[i] = matFAI(n2z[i], d2, k0[i])
    matFAI3[i] = matFAI(n3z[i], d3, k0[i])
    matFAI4[i] = matFAI(n4z[i], d4, k0[i])
    matFAI2[i] = matFAI(n2z[i], distance[1], k0[i])
    matFAI3[i] = matFAI(n3z[i], distance[2], k0[i])
    matFAI4[i] = matFAI(n4z[i], distance[3], k0[i])
    matFAI_array[1][i] = matFAI(n2z[i], distance[1], k0[i])
    matFAI_array[2][i] = matFAI(n3z[i], distance[2], k0[i])
    matFAI_array[3][i] = matFAI(n4z[i], distance[3], k0[i])
    matFAI_array[1][i] = matFAI(nz_array[1][i], distance[1], k0[i])
    matFAI_array[2][i] = matFAI(nz_array[2][i], distance[2], k0[i])
    matFAI_array[3][i] = matFAI(nz_array[3][i], distance[3], k0[i])
    """
    
    for j in range(1, layer_num - 1):
        matFAI_array[j][i] = matFAI(nz_array[j][i], distance[j], k0[i])

    # matTs[i] = mMats54[i] @ matFAI4[i] @ mMats43[i] @ matFAI3[i] \
    #    @ mMats32[i] @ matFAI2[i] @ mMats21[i]
    """
    matTs[i] = mMats_array[3][i] @ matFAI_array[3][i] \
        @ mMats_array[2][i] @ matFAI_array[2][i] \
        @ mMats_array[1][i] @ matFAI_array[1][i] \
        @ mMats_array[0][i] @ matFAI_array[0][i]
    """

    matTs[i] = eye(2)  # 一旦単位行列に
    for j in range(0, layer_num - 1):
        matTs[i] = mMats_array[j][i] @ matFAI_array[j][i] @ matTs[i]

    # matTp[i] = mMatp54[i] @ matFAI4[i] @ mMatp43[i] @ matFAI3[i] \
    #    @ mMatp32[i] @ matFAI2[i] @ mMatp21[i]
    '''
    matTp[i] = mMatp_array[3][i] @ matFAI_array[3][i] \
        @ mMatp_array[2][i] @ matFAI_array[2][i] \
        @ mMatp_array[1][i] @ matFAI_array[1][i] \
        @ mMatp_array[0][i]
    '''

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

axis([300, 999, 0, 0.2])

tight_layout()
show()
