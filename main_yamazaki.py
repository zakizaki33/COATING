import numpy as np
import vectrcaluculate3
import circle


def calc_area2(r):
    111111
    return r ** 2 * 3.14


print("はろーなつめさん")

Area1 = circle.calc_area(10)
print(Area1)


Area2 = calc_area2(10)
print(Area2)


# print(vectrcaluculate3.test1())

# 画角
d0 = np.array((0, np.sin(np.pi / 180), np.cos(np.pi / 180)))

print(d0)

# 始点
a0 = np.array((0.0, 0.0, 0.0))

a0[1] = 1.2

print(a0[1])


# 第一面中心
r1 = np.array((1, 1, 79))
# 第一面曲率半径
R1 = 100

# 屈折率
n0 = 1  # 前
n1 = 1.5  # 後

# p1=vectrcaluculate3.vector(d0,a0,r1,R1,1,1.5)
# print(p1[1])
