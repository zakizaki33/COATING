import scipy as sp
import numpy as np
import matplotlib as mp1
import matplotlib.pyplot as plt
from scipy import pi ,sin ,cos, tan,exp,arcsin,linspace,arange,sqrt,zeros,array,matrix,asmatrix
from matplotlib.pyplot import plot,show,xlabel,ylabel,title,legend,grid,axis,tight_layout,grid,axis

def matrixformat (n1,n2,n3,n4,n5,d2,d3,d4,WL,t):
 def mMATs(n1z,n2z):
    return(1/(2*n1z))*matrix([[n1z+n2z,n1z-n2z],[n1z-n2z,n1z+n2z]])

 def mMATp(n1z,n2z,n1,n2):
    return(1/(2*n1*n2*n1z))*\
        matrix([[n1**2*n2z+n2**2*n1z,n1**2*n2z-n2**2*n1z],[n1**2*n2z-n2**2*n1z,n1**2*n2z+n2**2*n1z]])

 def matFAI(k0,n1z,d1):
    return matrix([[exp(1j*n1z*k0*d1),0],[0,exp(-1j*n1z*k0*d1)]])

 


  #媒質1の屈折率
  #媒質2 "
 



 
 k0=2*pi/WL
 t1=t/180*pi
 s1=sin(t1)
 c1=cos(t1)
 s2=n1/n2*s1
 c2=sqrt(1-s2**2)
 s3=n1/n3*s1
 c3=sqrt(1-s3**2)
 s4=n1/n4*s1
 c4=sqrt(1-s4**2)
 s5=n1/n5*s1
 c5=sqrt(1-s5**2)

 n1z=n1*c1
 n2z=n2*c2
 n3z=n3*c3
 n4z=n4*c4
 n5z=n5*c5

 mMats21=zeros((2,2),dtype=complex)
 mMats32=zeros((2,2),dtype=complex)
 mMats43=zeros((2,2),dtype=complex)
 mMatp21=zeros((2,2),dtype=complex)
 mMatp32=zeros((2,2),dtype=complex)
 mMatp43=zeros((2,2),dtype=complex)
 matFAI2=zeros((2,2),dtype=complex)
 matFAI3=zeros((2,2),dtype=complex)
 matFAI4=zeros((2,2),dtype=complex)
 matTs=zeros((2,2),dtype=complex)
 matTp=zeros((2,2),dtype=complex)
 

 mMats21=mMATs(n2z,n1z)
 mMats32=mMATs(n3z,n2z)
 mMats43=mMATs(n4z,n3z)
 mMats54=mMATs(n5z,n4z)
 mMatp21=mMATp(n2z,n1z,n2,n1)
 mMatp32=mMATp(n3z,n2z,n3,n2)
 mMatp43=mMATp(n4z,n3z,n4,n3)
 mMatp54=mMATp(n5z,n4z,n5,n4)

 matFAI2=matFAI(k0,n2z,d2)
 matFAI3=matFAI(k0,n3z,d3)
 matFAI4=matFAI(k0,n4z,d4)
    
 matTs=mMats32@matFAI2@mMats21
 matTs=mMats43@matFAI3@matTs
 matTs=mMats54@matFAI4@matTs

 matTp=mMatp32@matFAI2@mMatp21
 matTp=mMatp43@matFAI3@matTp
 matTp=mMatp54@matFAI4@matTp


 rs=-matTs[1,0]/matTs[1,1]
 ts=matTs[0,0]-matTs[0,1]*matTs[1,0]/matTs[1,1]

 rp=-matTp[1,0]/matTp[1,1]
 tp=matTp[0,0]-matTp[0,1]*matTp[1,0]/matTp[1,1]
    
     
 RsAbs=abs(rs)**2
 RpAbs=abs(rp)**2

 TsAbs=abs(ts)**2
 TpAbs=abs(tp)**2
 R=(RsAbs**2+RpAbs**2)**0.5
 deg=np.arctan(rs/rp)*180/pi

 return(RsAbs,RpAbs,TsAbs,TpAbs)
 
#plot(WL,R,label="R")






