
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, arcsin, linspace
from matplotlib.pyplot import (
    plot, show, xlabel, ylabel, title, legend, grid, axis, tight_layout
)

n1 = 1
n2 = 1.5

t1Deg = linspace(0, 90, 91)
t1 = t1Deg / 180 * pi
t2 = arcsin((n1 / n2) * sin(t1))

tp = 2 * n1 * cos(t1) / (n2 * cos(t1) + n1 * cos(t2))
rp = (n2 * cos(t1) - n1 * cos(t2)) / (n2 * cos(t1) + n1 * cos(t2))
ts = 2 * n1 * cos(t1) / (n1 * cos(t1) + n2 * cos(t2))
rs = (n1 * cos(t1) - n2 * cos(t2)) / (n1 * cos(t1) + n2 * cos(t2))

Rp = rp**2
Tp = tp ** 2 * (n2 * cos(t2)) / (n1 * cos(t1))
Rs = rs**2
Ts = ts ** 2 * (n2 * cos(t2)) / (n1 * cos(t1))

plt.figure(figsize=(8, 6))
plot(t1Deg, Rp, label=r"$R_{12}^{\rm{p}}$", linewidth=3.0, color='black',
     linestyle='dashed')
plot(t1Deg, Tp, label=r"$T_{12}^{\rm{p}}$", linewidth=3.0, color='black',
     linestyle='solid')
plot(t1Deg, Rs, label=r"$R_{12}^{\rm{s}}$", linewidth=3.0, color='gray',
     linestyle='dashed')
plot(t1Deg, Ts, label=r"$T_{12}^{\rm{s}}$", linewidth=3.0, color='gray',
     linestyle='solid')

xlabel(r"$\theta_1$(deg.)", fontsize=20)
ylabel(r"$R, T$", fontsize=20)
title("Reflectivity and Transmittance", fontsize=18)
legend(fontsize=20, loc='lower left')
grid(True)

axis([0.0, 90, 0, 1.1])

tight_layout()
show()
