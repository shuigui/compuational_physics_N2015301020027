import pylab as pl
import math as math
m=1
q=0.5
l=9.8
g=9.8
D=2/3
dt=0.04
w=[0 for x in range(0,350000)]
b=[0 for x in range(0,350000)]
t=[0 for x in range(0,350000)]
F=[]
y=[]
w[0]=0
b[0]=0.2
t[0]=0
for j in range(0,301):
    FD = 1.35 + 0.0005*j
    for i in range(0,350000-1):
        w[i+1]=w[i]-((g/l)*math.sin(b[i])+q*w[i]-FD*math.sin(D*t[i]))*dt
        b[i+1]=b[i]+w[i+1]*dt
        if b[i+1]<-math.pi:
            b[i+1]=b[i+1]+2*math.pi
        elif b[i+1]>math.pi:
            b[i+1]=b[i+1]-2*math.pi
        else:
            b[i+1]=b[i+1]    
        t[i+1]=t[i]+dt
        if (t[i+1]>900*math.pi)and((D*t[i+1])/(2*math.pi)-int((D*t[i+1])/(2*math.pi))<(D*dt)/(2*math.pi)):
            y.append(b[i+1])
            F.append(FD)
pl.scatter(F,y,s=1)
pl.show()

     
     
     
     
     
     
     
     
     
     
     
     
 
