
# import scipy as sp
# import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, linspace, sqrt
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, legend,
                               grid, axis, tight_layout)

n1 = 1.5
n2 = 1.0
ep1 = n1 ** 2
ep2 = n2 ** 2

t1Deg = linspace(0, 90, 90)
t1 = t1Deg / 180 * pi

s1 = sin(t1)  # sin(t1)
c1 = cos(t1)  # cos(t1)
s2 = n1 / n2 * s1  # sin(t2)
c2 = sqrt(1 - s2**2)  # cos(t2)

n1z = n1 * c1
n2z = n2 * c2

rs = (n1z - n2z) / (n1z + n2z)
rp = (ep2 * n1z - ep1 * n2z) / (ep2 * n1z + ep1 * n2z)

RsAbs = abs(rs ** 2)
RpAbs = abs(rp ** 2)

plt.figure(figsize=(8, 6))
plot(t1Deg, RpAbs, label=r"$R_{12}^{\rm{p}}$", linewidth=3.0,
     linestyle='dashed')
plot(t1Deg, RsAbs, label=r"$R_{12}^{\rm{s}}$", linewidth=3.0,
     linestyle='solid')
xlabel(r"$\theta_1$(deg.)", fontsize=20)
ylabel(r"$R, T$", fontsize=20)
title("Reflectivity", fontsize=18)
legend(fontsize=20, loc='lower right')
grid(True)
axis([0.0, 90, 0, 1.1])
tight_layout()
show()
