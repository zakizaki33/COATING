import numpy as np
import Functions


def vectr(d, a, r, R, n1, n2):
    # d(xd yd zd) :方向ベクトル
    # a(xa ya za) :位置ベクトル
    # r(xr yr zr) :球の中心
    # R           :球の半径
    # n1,n2       :屈折率

    # At^2+2Bt+C=0より
    A = np.dot(d, d)
    B = np.dot(a - r, d)
    C = np.dot(a - r, a - r) - R**2

    discriminant = B**2 - A * C
    if discriminant < 0:
        print("解なし エラー発生")
        exit()
    else:
        # ここでtの値が導出(解の公式より)
        t1 = (-B - np.sqrt(discriminant)) / A
        t2 = (-B + np.sqrt(discriminant)) / A
        t = np.min([t1, t2]) if R > 0 else np.max([t1, t2])

        # 交点の座標:p(x,y,z)=a+td
        p0 = a + t * d

    hosen = (p0 - r) if R > 0 else (r - p0)

    # 屈折ベクトルを計算する前準備
    Dx = d / np.sqrt(np.dot(d, d))
    hosen = hosen / np.sqrt(np.dot(hosen, hosen))
    n = n1 / n2
    ref_vect = (n * Dx - n * hosen * (np.dot(Dx, hosen) +
                                      np.sqrt((1 / n)**2 -
                                      1 +
                                      np.dot(Dx, hosen)**2)))

    # r 球の中心
    # p0 交点座標
    # ref_vect 屈折ベクトル
    return (r, p0, ref_vect)

def main():
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

    # 画角の範囲
    deg = np.linspace(0.000001, 2.292442776, 99)
    D0 = np.transpose(np.array([np.zeros(99),
                                np.sin(np.radians(deg)),
                                np.cos(np.radians(deg))]))

    # 数値置き場
    list1_radius_pos = np.zeros((number, 3))  # 球の中心
    list2_cross_pos = np.zeros((number, 3))  # 交点
    list3_ref_vector = np.zeros((number, 3))  # 屈折ベクトル

    # 収差計算に関するパラメータを入れる枠
    point = np.zeros((99, 3), float)  # 交点(像面-1 面)
    ref_vector = np.zeros((99, 3), float)  # 屈折ベクトル（像面-1 面）
    SCA = np.zeros((99, 1), float)  # 球面収差

    for j in range(0, 99, 1):  # 画角を0~2.29244 degまで振る

        refract_info = vectr(D0[j],
                            a0,
                            np.array((a0[0], a0[1], d0 + lens_data[0, 0])),
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
                        d0 + np.sum(lens_data[:i + 1, 2]) + lens_data[i + 1, 0])
                        )

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

        # 球面収差の計算
        point[j] = list2_cross_pos[number - 2, :]  # （像面-1）面の交点
        ref_vector[j] = list3_ref_vector[number - 2, :]  # （像面-1）面の屈折ベクトル
        value = point[j, 2] + (ref_vector[j, 2] * point[j, 1] /
                               abs(ref_vector[j, 1]))
        value_axis = point[0, 2] + (ref_vector[0, 2] * point[0, 1] /
                                    abs(ref_vector[0, 1]))
        SCA[j] = value - value_axis
 
    # SCAを描画する
    Functions.plotSCA(SCA)

    tracker = (list2_cross_pos, list3_ref_vector)
    np.savetxt('球面収差.txt', SCA)
    np.savetxt('光線追跡vector.txt', tracker[1])

if __name__ == "__main__":
    main()
 
    

