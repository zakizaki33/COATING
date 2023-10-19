import numpy as np
import Functions


def vectr(d, a, r, R, n1, n2):
    # d(xd yd zd) :方向ベクトル，a(xa ya za): 位置ベクトル，
    # r(xr yr zr) :球の中心 球の半径:R,屈折率:n1,n2
    # At^2+2Bt+C=0より
    A = d[0]**2 + d[1]**2 + d[2]**2
    B = (a[0] - r[0]) * d[0] + (a[1] - r[1]) * d[1] + (a[2] - r[2]) * d[2]
    C = (a[0] - r[0])**2 + (a[1] - r[1])**2 + (a[2] - r[2])**2 - R**2
    # print(A,B,C)

    if B**2 - A * C < 0:
        # print(B**2 - A * C)
        print("解なし エラー発生")
        exit()
    else:
        # t = np.array(((-B + (B**2 - A * C)**0.5) / A,
        #               (-B - (B**2 - A * C)**0.5) / A), float)
        
        t = np.array(((-B + (B**2 - A * C)**0.5) / A,
                      (-B - (B**2 - A * C)**0.5) / A))
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

    ref_vect = (n1 / n2) * Dx - (n1 / n2) * ((np.dot(Dx, hosen)) + (((n2 / n1)**2 - 1 + np.dot(Dx, hosen)**2)**0.5)) * hosen  # 屈折ベクトル

    # r 球の中心
    # D 交点座標
    # ref_vect 屈折ベクトル
    return (r, D, ref_vect)

    # P=np.min(P[:,2]>0)


# レンズデータ
a0 = np.array((0, 0, 0))
d0 = 100
n0 = 1
# ここにパラメータを入力（axis=0方向:第i面　axis=1方向:曲率，屈折率，厚み）
lens_data = np.array([(11.050, 1.744003267, 5.50),
                 (22.680, 1, 0.450),
                 (-29.530, 1.7400050237, 0.850),
                 (11.580, 1, 1.660),
                 (27.530, 1.744003267, 1.600),
                 (-18.100, 1, 46.700),
                 (1000000, 1, 10000)],
                float)
# レンズ面の数
number = np.shape(lens_data)[0]

# 数値置き場
list1_radius_pos = np.zeros((number - 0, 3))  # 球の中心
list2_cross_pos = np.zeros((number - 0, 3))  # 交点
list3_ref_vector = np.zeros((number - 0, 3))  # 屈折ベクトル

# 収差計算に関するパラメータを入れる枠
point = np.zeros((99, 3), float)  # 交点(像面-1 面)
ref_vector = np.zeros((99, 3), float)  # 屈折ベクトル（像面-1 面）
zz = np.zeros((99, 1), float)  # z補正
z_imagey = np.zeros((99, 1), float)  # 中心軸との交点　（像面付近）
D0 = np.zeros((99, 3), float)  # 画角
SCA = np.zeros((99, 1), float)  # 球面収差
SCA2 = np.zeros((99, 1), float)  # 球面収差


# deg = np.linspace(2.292442776, 2.292442766, 1)
deg = np.linspace(0.000001, 2.292442776, 99)  # 画角の範囲（deg）

for j in range(0, 99, 1):  # [0]: #画角を0-2.29244 deg振る
    D0[j] = np.array((0, np.sin(np.radians(deg[j])),
                      np.cos(np.radians(deg[j]))))  # 画角

    refract_info = vectr(D0[j],
                        a0,
                        np.array((a0[0], a0[1], d0 + lens_data[0, 0])), # 第１面の球心
                        lens_data[0, 0],
                        n0,
                        lens_data[0, 1])
    
    list1_radius_pos[0] = refract_info[0]  # 1面の球の中心
    list2_cross_pos[0] = refract_info[1]  # 1面の交点
    list3_ref_vector[0] = refract_info[2]  # 1面の屈折ベクトル

    # 第1面以降の計算
    for i in range(0, number - 1, 1):
        rx = np.array((list1_radius_pos[i, 0],
                       list1_radius_pos[i, 1],
                       # i面の球の中心
                       d0 + np.sum(lens_data[:i + 1, 2]) + lens_data[i + 1, 0]))
                     
        refract_info = vectr(list3_ref_vector[i, :],
                   list2_cross_pos[i, :],
                   rx,
                   lens_data[i + 1, 0],
                   lens_data[i, 1],
                   lens_data[i + 1, 1])  # i-1_i面の光線追跡
        
        list1_radius_pos[i + 1] = refract_info[0]  # i面の球の中心
        list2_cross_pos[i + 1] = refract_info[1]  # i面の交点
        list3_ref_vector[i + 1] = refract_info[2]  # i面の屈折ベクトル

    print("Trial", j, "times")
    print("Surface Intersection Point (x, y, z):")
    print(list2_cross_pos)
    # print(list3_ref_vector)
    # exit()
    
    # 球面収差の計算
    point[j] = list2_cross_pos[number - 2, :]  # （像面-1）面の交点
    ref_vector[j] = list3_ref_vector[number - 2, :]  # （像面-1）面の屈折ベクトル

    zz[j] = point[j, 2] - point[0, 2]  # z補正
    z_imagey[j] = np.dot(point[j, 1],ref_vector[j, 1]) / ref_vector[j, 2] - zz[j]  # 中心軸交点
    SCA[j] = z_imagey[j] - z_imagey[0]  # 球面収差

    # 球面収差の計算その２
    # value = point[j, 2]+ ref_vector[j,2]*point[j, 1]/abs(ref_vector[j,1])
    # value_axis =point[0, 2]+ ref_vector[0,2]*point[0, 1]/abs(ref_vector[0,1])
    # SCA2[j]=value- value_axis

    
# SCAを描画する
'''
print(point[98])
print(ref_vector[98])
value = point[98, 2]+ ref_vector[98,2]*point[98, 1]/abs(ref_vector[98,1])
value_axis =point[0, 2]+ ref_vector[0,2]*point[0, 1]/abs(ref_vector[0,1])
SCA2[98]=value- value_axis
'''

Functions.plotSCA(SCA)
# Functions.plotSCA(SCA2)


tracker = (list2_cross_pos, list3_ref_vector)
np.savetxt('球面収差.txt', SCA)
np.savetxt('光線追跡vector.txt', tracker[1])
