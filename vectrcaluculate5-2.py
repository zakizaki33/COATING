import numpy as np
# import matplotlib.pyplot as plt


def vectr(d, a, r, R, n1, n2):
    # d(xd yd zd) :方向ベクトル，a(xa ya za): 位置ベクトル，
    # r(xr yr zr) :球の中心 球の半径:R,屈折率:n1,n2
    # At^2+2Bt+C=0より
    A = d[0]**2 + d[1]**2 + d[2]**2
    B = (a[0] - r[0]) * d[0] + (a[1] - r[1]) * d[1] + (a[2] - r[2]) * d[2]
    C = (a[0] - r[0])**2 + (a[1] - r[1])**2 + (a[2] - r[2])**2 - R**2
    # print(A,B,C)

    if B**2 - A * C < 0:
        print(B**2 - A * C)
        print("解なし")
        exit()
    else:
        t = np.array(((-B + (B**2 - A * C)**0.5) / A,
                      (-B - (B**2 - A * C)**0.5) / A), float)
        # print(t)#ここでtの値が導出(解の公式より)
        # t=int(np.amin(t>0))

        if R > 0:
            t = np.min(t)
            # print(t)
        else:
            t = np.max(t)
            # print (t)
        # print(t)
        # exit()

        p0 = np.array((a[0] + t * d[0], a[1] + t * d[1], a[2] + t * d[2]))
        # 交点の座標:p(x,y,z)=a+td
        # p1=np.array((xa+t[1]*xd,ya+t[1]*yd,za+t[1]*zd))

        # print(P)
    D = np.array((p0[0], p0[1], p0[2]))  # 交点座標
    RO = np.array((r[0], r[1], r[2]))  # 球の中心座標

    if R > 0:
        hosen = D - RO
    else:
        hosen = RO - D

    Dx = d / (d[0]**2 + d[1]**2 + d[2]**2)**0.5
    hosen = hosen / (hosen[0]**2 + hosen[1]**2 + hosen[2]**2)**0.5
    # print(hosen)
    # print("法線ベクトル")
    # 屈折ベクトル
    p1 = ((n1 / n2) * Dx - (n1 / n2) * (np.dot(Dx, hosen) + (
        ((n2 / n1)**2 - 1 + ((np.dot(Dx, hosen))**2))**0.5))) * hosen

    # r 球の中心
    # D 交点座標
    # p1 屈折ベクトル
    return (r, D, p1)

    # P=np.min(P[:,2]>0)


# ここにパラメータを入力（axis=0方向:第i面　axis=1方向:曲率，屈折率，厚み）
# レンズデータ
data = np.array([(11.050, 1.74, 5.50),
                 (22.680, 1, 0.450),
                 (-29.530, 1.74, 0.850),
                 (11.580, 1, 1.660),
                 (27.530, 1.74, 1.600),
                 (-18.100, 1, 46.700),
                 (1000000, 1, 10000)],
                float)
# レンズ面の数
number = np.shape(data)[0]

# 0面
point = np.zeros((99, 3), float)
ref_vector = np.zeros((99, 3), float)
zz = np.zeros((99, 1), float)
z_imagey = np.zeros((99, 1), float)
SCA = np.zeros((99, 1), float)
D0 = np.zeros((99, 3), float)
# deg=np.linspace(2.29244,2.29244,1)
deg = np.linspace(0, 2.29244, 100)


for x in range(0, 99, 1):
    D0[x] = np.array((0, np.sin(deg[x] * np.pi / 180),
                      np.cos(deg[x] * np.pi / 180)))  # 画角
    a0 = np.array((0, 0, 0))
    d0 = 100
    n0 = 1

    anglenumber = np.shape(D0[x])[0]

    # 数値置き場
    list1 = np.zeros((number - 1, 3))  # 球の中心
    list2 = np.zeros((number - 1, 3))  # 交点
    list3 = np.zeros((number - 1, 3))  # 屈折ベクトル
    r1 = np.array((a0[0], a0[1], d0 + data[0, 0]))  # １面球の中心

    # 物体面から第1面までは別計算
    p1 = vectr(D0[x], a0, r1, data[0, 0], n0, data[0, 1])
    # print(p1)
    list1[0] = p1[0]  # 1面の球の中心
    list2[0] = p1[1]  # 1面の交点
    list3[0] = p1[2]  # 1面の屈折ベクトル

    # 第1面以降の計算
    for i in range(0, number - 2, 1):
        rx = np.array((list1[i, 0],
                       list1[i, 1],
                       # i面の球の中心
                       d0 + np.sum(data[:i + 1, 2]) + data[i + 1, 0]))
                     
        px = vectr(list3[i, :],
                   list2[i, :],
                   rx,
                   data[i + 1, 0],
                   data[i, 1],
                   data[i + 1, 1])  # i-1_i面の光線追跡
        list1[i + 1] = px[0]  # i面の球の中心
        list2[i + 1] = px[1]  # i面の交点
        list3[i + 1] = px[2]  # i面の屈折ベクトル
    
    print("i面の交点 x, y, z")
    print(list2)
    # print(list3)
    # exit()
    
    '''
    # 球面収差の計算
    point[x] = list2[number - 2, :]
    ref_vector[x] = list3[number - 2, :]

    zz[x] = ref_vector[x, 2] - ref_vector[0, 2]
    z_imagey[x] = np.dot(point[x, 2], point[x, 1]) / ref_vector[x, 2]
    SCA[x] = z_imagey[x] - zz[x]
    '''

# print(SCA)
# plt.plot(SCA)
# plt.show()

# tracker=(list2,list3)

# np.savetxt('球面収差.txt', SCA)
# np.savetxt('光線追跡vector.txt',tracker[1])

# 変更させてみる（やまざき　2023-10-04）

# 変更させてみる（やまざき　2023-10-05）
