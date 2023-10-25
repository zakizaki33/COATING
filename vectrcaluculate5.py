import numpy as np

# d(xd yd zd) :方向ベクトル，a(xa ya za): 位置ベクトル，r(xr yr zr) :球の中心ベクトル, r:球の曲率半径, n1:屈折率, n2:屈折率
def vectr(d, a, r, R, n1, n2):  # 関数を定義
    
    # At^2 + 2Bt + C = 0より
    A = d[0]**2 + d[1]**2 + d[2]**2
    B = (a[0] - r[0]) * d[0] + (a[1] - r[1]) * d[1] + (a[2] - r[2]) * d[2]
    C = (a[0] - r[0])**2 + (a[1] - r[1])**2 + (a[2] - r[2])**2 - R**2
    
    # 解の公式の判断（判別式）
    if B**2 - A * C < 0:
        print(B**2 - A * C)
        print("判別式が負になりました。プログラムを停止します")
        exit()
    else:
        # print(t)#ここでtの値が導出(解の公式より)
        t = np.array(((-B + (B**2 - A * C)**0.5) / A, (-B - (B**2 - A * C)**0.5) / A))
        
        # 凹面凸面の判断??
        if R > 0:
            t = np.min(t)
            # print(t)
        else:
            t = np.max(t)
            # print(t)
        
        p0 = np.array((a[0] + t * d[0], a[1] + t * d[1], a[2] + t * d[2]))  # 交点の座標:p(x,y,z)=a+td
        # p1=np.array((xa+t[1]*xd,ya+t[1]*yd,za+t[1]*zd))
        #P = np.array((p0))
        # print(P)
    D = np.array((p0[0], p0[1], p0[2]))  # 交点座標
    RO = np.array((r[0], r[1], r[2]))  # 球の中心座標

    if R > 0:
        hosen = D - RO
    else:
        hosen = RO - D
    
    # 規格化
    Dx = D / ((D[0]**2 + D[1]**2 + D[2]**2)**0.5)
    hosen = hosen / (hosen[0]**2 + hosen[1]**2 + hosen[2]**2)**0.5
    print("法線ベクトル", hosen)

    # p1 = (n1 / n2) * Dx - (n1 / n2) * ((np.dot(Dx, hosen)) + (((n2 / n1)**2 - 1 + np.dot(Dx, hosen)**2)**0.5)) * hosen  # 屈折ベクトル
    p1_ = (n1 / n2) * Dx - (n1 / n2) * ((np.dot(Dx, hosen)) + (((n2 / n1)**2 - 1 + np.dot(Dx, hosen)**2)**0.5)) * hosen  # 屈折ベクトル

    return(D, p1_)


# ここにパラメータを入力

# 0面
D0 = np.array((0, np.sin(np.radians(2.29244)), np.cos(np.radians(2.29244))))  # 画角
a0 = np.array((0, 0, 0))  # 始点
d0 = 100  # 厚み(1面までの距離)
# 屈折率
n0 = 1.000  # 0面

# 1面
R1 = 11.05  # 曲率半径
r1 = np.array((0, 0, d0 + R1))  # 球の中心
n1 = 1.744003267  # 屈折率
d1 = 5.5  # 厚み
# 2面
R2 = 22.68  # 曲率半径
n2 = 1.000  # 屈折率
r2 = np.array((r1[0], r1[1], d0 + d1 + R2))  # 球の中心

print("一面")
p1 = vectr(D0, a0, r1, R1, n0, n1)
print("交点，屈折ベクトル")
print(p1, "\n")

print("二面")
p2 = vectr(p1[1], p1[0], r2, R2, n1, n2)
print("交点，屈折ベクトル")
print(p2, "\n")

