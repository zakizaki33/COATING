import numpy as np


def vectr(d, a, r, R, n1, n2):  # 関数を定義
    # d(xd yd zd) :方向ベクトル，a(xa ya za): 位置ベクトル，r(xr yr zr) :球の中心 r:球の半径,n1,n2:屈折率
 


 # At^2+2Bt+C=0より
 A = d[0]**2+d[1]**2+d[2]**2
 B = (a[0]-r[0])*d[0]+(a[1]-r[1])*d[1]+(a[2]-r[2])*d[2]
 C = (a[0]-r[0])**2+(a[1]-r[1])**2+(a[2]-r[2])**2-R**2
 #print(A,B,C)
 
 
 if B**2-A*C<0:
     print(B**2-A*C)
     exit()
 else: 
     t=np.array(((-B+(B**2-A*C)**0.5)/A,(-B-(B**2-A*C)**0.5)/A))
     #print(t)#ここでtの値が導出(解の公式より)
     #t=int(np.amin(t>0))
     
     t=np.min(t)
     #print(t)
  
     #print(t)
     #exit()
     
     

     p0=np.array((a[0]+t*d[0],a[1]+t*d[1],a[2]+t*d[2])) #交点の座標:p(x,y,z)=a+td
     #p1=np.array((xa+t[1]*xd,ya+t[1]*yd,za+t[1]*zd))
     P=np.array((p0))
     #print(P)
 D=np.array((d[0],d[1],d[2]))#交点座標
 R=np.array((r[0],r[1],r[2]))#球の中心座標
 hosen=p0-R
 hosen=hosen/(hosen[0]**2+hosen[1]**2+hosen[2]**2)**0.5
 #print(hosen)

 p1=(n1/n2)*D-(n1/n2)*((np.dot(D,hosen))+(((n2/n1)**2-1+np.dot(D,hosen)**2)**0.5))*hosen
 
 
 return(D,p1)

 
 #P=np.min(P[:,2]>0)

#ここにパラメータを入力
 
#0面
D0=np.array((0,np.sin(np.pi/180),np.cos(np.pi/180)))#画角
a0=np.array((0,0,0))#始点
d0=50#厚み(1面までの距離)
#屈折率
n0=1#0面


#1面
R1=100#曲率半径
r1=np.array((0,0,d0+R1))#球の中心
n1=1.5#屈折率
d1=10#厚み
#2面
R2=-100#曲率半径
n2=1#屈折率
r2=np.array((r1[0],r1[1],r1[2]+R2+d1))#球の中心



p1=vectr(D0,a0,r1,R1,n0,n1)
print("一面（交点，屈折ベクトル）")
print("")
print(p1)

p2=vectr(p1[1],p1[0],r2,R2,n1,n2)
print("二面（交点，屈折ベクトル）")
print("")
print(p2)

print("test")
print((p2[1][0])**2 + (p2[1][1])**2 + (p2[1][2])**2)

exit()
P=vectr(0,np.sin(np.pi/180),np.cos(np.pi/180),0,0,0,1,1,79,100,1,1.5)#ここに任意の値を入れる
print(P)


 


 


