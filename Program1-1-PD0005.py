
# import scipy as sp
# import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import pi, sin, cos, arcsin, linspace
from matplotlib.pyplot import (plot, show, xlabel, ylabel, title, legend,
                               grid, axis, tight_layout)

n1 = 1
n2 = 1.5

t1Deg = linspace(0, 90, 91)
t1 = t1Deg / 180 * pi
t2 = arcsin((n1 / n2) * sin(t1))

tp = 2 * n1 * cos(t1) / (n2 * cos(t1) + n1 * cos(t2))
rp = (n2 * cos(t1) - n1 * cos(t2)) / (n2 * cos(t1) + n1 * cos(t2))
ts = 2 * n1 * cos(t1) / (n1 * cos(t1) + n2 * cos(t2))
rs = (n1 * cos(t1) - n2 * cos(t2)) / (n1 * cos(t1) + n2 * cos(t2))

plt.figure(figsize=(8, 6))
plot(t1Deg, rp, label=r"$r_{12}^{\rm{p}}$", linewidth=3.0, color='black',
     linestyle='dashed')

xlabel(r"$\theta_1$(deg.)", fontsize=20)
ylabel(r"$r, t$", fontsize=20)
title("Reflection and Transmission Coefficient", fontsize=18)
legend(fontsize=20, loc='lower right')
grid(True)

axis([0.0, 90, -1, 1])

tight_layout()
show()

"""
import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
import coattheory
def N (A,B,C,WL):
   return(A+B/(WL**2)+C/(WL**4))
def N_OHARA(A1,A2,A3,WL,B1,B2,B3):
   return((A1*(WL**2))/(WL**2-B1)+(A2*(WL**2))/(WL**2-B2)+(A3*(WL**2))/(WL**2-B3))



t1start=300
t1end=1000
t1points=700

WL=linspace(t1start,t1end,t1points)

matrixRP=np.zeros((t1points,t1points))
for i in range(t1points):
 n1=N_OHARA(1.15150190,1.18583612*(10**(-1)),1.26301359,WL[i],1.05984130*(10**(-2)),-1.18225190*(10**(-2)),1.29617662*(10**2))
 n2=N(2.266566,20626.89,6.29*10**9,WL[i])
 n3=N(1.457341,3417.464,0,WL[i])
 n4=N(2.266566,20626.89,6.29*10**9,WL[i])
 n5=1
 d2=57.42
 d3=93.6
 d4=57.42
 t=0
 #print(WL[i])
  
 matrix1= coattheory.matrixformat(n1,n2,n3,n4,n5,d2,d3,d4,WL,t)
 #print(matrix1[1])
 
 

plt.plot(WL,matrix1[2])
plt.show()

"""
