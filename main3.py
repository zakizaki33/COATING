from tkinter import END
from turtle import end_fill
import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi ,sin ,cos, tan,exp,arcsin,linspace,arange,sqrt,zeros,array,matrix,asmatrix
from matplotlib.pyplot import plot,show,xlabel,ylabel,title,legend,grid,axis,tight_layout,grid,axis
# import coattheory
# import fitting
import coatematrix
import coatematrix1

def N (A,B,C,WL):
   return(A+B/(WL**2)+C/(WL**4))
def N_OHARA(A1,A2,A3,WL,B1,B2,B3):
   return((A1*(WL**2))/(WL**2-B1)+(A2*(WL**2))/(WL**2-B2)+(A3*(WL**2))/(WL**2-B3))



def matrix_calucue(WL):

 n1=1.52#N_OHARA(1.15150190,1.18583612*(10**(-1)),1.26301359,WL,1.05984130*(10**(-2)),-1.18225190*(10**(-2)),1.29617662*(10**2))#基盤屈折率
 n2=1.63#N(2.266566,20626.89,6.29*10**9,WL) #1層　屈折率
 n3=2.10#N(1.457341,3417.464,0,WL)# 2層　屈折率
 n4=1.38#N(2.266566,20626.89,6.29*10**9,WL) #3層　屈折率
 n5=1#空気
 d2=84.35#膜の厚み(１層)
 d3=130.95# （2層）""
 d4=99.64# (3層)""
 
 t4=30#入射角
 t3=arcsin((n5/n4)*sin(t4))#屈折角
 t2=arcsin((n4/n3)*sin(t3))# "
 t1=arcsin((n3/n2)*sin(t2))# "

 
 #s偏光
 #膜光線計算
 #print(matrix1)
 matrix1=coatematrix1.matrixformat1(n5,n4,t4)[0]#一層目と空気の境界
 matrix1=coatematrix.matrixformatX(n4,n4,d4,WL,t3,0)[0]@matrix1#1層目*(1-1):屈折率が異なる境界面を差し引く
 matrix1=coatematrix.matrixformatX(n4,n3,d4,WL,t3,1)[0]@matrix1#1層目2層目の境界
 matrix1=coatematrix.matrixformatX(n3,n3,d3,WL,t3,2)[0]@matrix1#2層目*(3-1):屈折率が異なる境界面を差し引く
 matrix1=coatematrix.matrixformatX(n3,n2,d3,WL,t2,1)[0]@matrix1#2層目3層目の境界
 matrix1=coatematrix.matrixformatX(n2,n2,d3,WL,t2,0)[0]@matrix1#3層目*(1-1):屈折率が異なる境界面を差し引く
 matrix1=coatematrix.matrixformatX(n2,n1,d2,WL,t1,1)[0]@matrix1#3層目基盤の境界
 #print(matrix1)
 
 rs=-matrix1[1,0]/matrix1[1,1]
 ts=matrix1[0,0]-matrix1[0,1]*matrix1[1,0]/matrix1[1,1]
 
 RsAbs=abs(rs)**2#反射率強度
 TsAbs=abs(ts)**2#透過率強度
 #print(RsAbs)
 
 #p偏光
 matrix2=coatematrix1.matrixformat1(n5,n4,t4)[1]#1層目2層目の境界
 matrix2=coatematrix.matrixformatX(n4,n3,d4,WL,t3,1)[1]@matrix2#1層目2層目の境界
 matrix2=coatematrix.matrixformatX(n3,n3,d3,WL,t3,2)[1]@matrix2 #2層目*(3-1):屈折率が異なる境界面を差し引く
 matrix2=coatematrix.matrixformatX(n3,n2,d3,WL,t2,1)[1]@matrix2#2層目3層目の境界
 matrix2=coatematrix.matrixformatX(n2,n1,d2,WL,t1,1)[1]@matrix2#4層目基盤の境界
 rp=-matrix2[1,0]/matrix2[1,1]#反射率
 tp=matrix2[0,0]-matrix2[0,1]*matrix2[1,0]/matrix2[1,1]#透過率
     
 RpAbs=abs(rp)**2#反射率強度
 
 TpAbs=abs(tp)**2#透過率強度


 R=(RsAbs**2+RpAbs**2)**0.5#無偏光
 T=(TsAbs**2+TpAbs**2)**0.5#無偏光
 #print(R)
 deg=np.arctan(rs/rp)*(180/pi) #偏光角

 return(RsAbs,RpAbs,TsAbs,TpAbs,R,T,deg) #s偏光反射率，s偏光透過率，p偏光透過率，p偏光反射率，無偏光反射率，無偏光透過率，偏光方向


#print(matrix1[2])
#plt.plot(WL,matrix1[2])
#plt.show()

#y=fitting.index("RefractiveIndexINFO.txt")
#print(y)

#波長設定
t1start=380#低波長
t1end=780#高波長
t1points=101#data point

#環境設定
WL=linspace(t1start,t1end,t1points)
matrixRS=np.zeros(t1points)
matrixRP=np.zeros(t1points)
matrixTS=np.zeros(t1points)
matrixTP=np.zeros(t1points)
matrixtAve=np.zeros(t1points)
for i in range (t1points):
    matrixrs=matrix_calucue(WL[i])[0]
    matrixrp=matrix_calucue(WL[i])[1]
    matrixts=matrix_calucue(WL[i])[2]
    matrixtp=matrix_calucue(WL[i])[3]
    matrixtave=matrix_calucue(WL[i])[5]
    #matrixRP=list(matrixRP,axis=0)
    matrixRS[i]=matrixrs
    matrixRP[i]=matrixrp
    
    matrixTS[i]=matrixts
    matrixTP[i]=matrixtp
    matrixtAve[i]=matrixtave
  

 
plt.plot(WL,matrixRS)
plt.plot(WL,matrixRP)
#plt.plot(WL,matrixTS)
#plt.plot(WL,matrixTP)
#plt.plot(WL,matrixAve)
plt.show()











