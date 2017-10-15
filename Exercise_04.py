# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 23:09:15 2017

@author: panxiang
"""

import pylab as pl
import math
y1 = [0]
y2 = [0]
y3 = [0]
y4 = [0]
y5 = [0]
y6 = [0]
x1 = [0]
x2 = [0]
x3 = [0]
x4 = [0]
x5 = [0]
x6 = [0]
v = 700
vx1 = [v*math.cos(math.pi/4)]
vx2 = [v*math.cos(30/180*math.pi)]
vx3 = [v*math.cos(35/180*math.pi)]
vx4 = [v*math.cos(40/180*math.pi)]
vx5 = [v*math.cos(50/180*math.pi)]
vx6 = [v*math.cos(55/180*math.pi)]
vy1 = [math.tan(math.pi/4)*vx1[0]]
vy2 = [vx2[0]*math.tan(30/180*math.pi)]
vy3 = [vx3[0]*math.tan(35/180*math.pi)]
vy4 = [vx4[0]*math.tan(40/180*math.pi)]
vy5 = [vx5[0]*math.tan(50/180*math.pi)]
vy6 = [vx6[0]*math.tan(55/180*math.pi)]
dt = 0.1
def f (a,b):
    return a + b*dt
def g(c):
    return c - 9.8*dt
for i in range(1,10000):
    x1i = f(x1[i-1],vx1[i-1]*dt)
    x2i = f(x2[i-1],vx2[i-1]*dt)
    x3i = f(x3[i-1],vx3[i-1]*dt)
    x4i = f(x4[i-1],vx4[i-1]*dt)
    x5i = f(x5[i-1],vx5[i-1]*dt)
    x6i = f(x6[i-1],vx6[i-1]*dt)
    vx1i = vx1[i-1]
    vx2i = vx2[i-1]
    vx3i = vx3[i-1]
    vx4i = vx4[i-1]
    vx5i = vx5[i-1]
    vx6i = vx6[i-1]
    y1i = f(y1[i-1],vy1[i-1])
    y2i = f(y2[i-1],vy2[i-1])
    y3i = f(y3[i-1],vy3[i-1])
    y4i = f(y4[i-1],vy4[i-1])
    y5i = f(y5[i-1],vy5[i-1])
    y6i = f(y6[i-1],vy6[i-1])
    vy1i = g(vy1[i-1])
    vy2i = g(vy2[i-1])
    vy3i = g(vy3[i-1])
    vy4i = g(vy4[i-1])
    vy5i = g(vy5[i-1])
    vy6i = g(vy6[i-1])
    x1.append(x1i)
    x2.append(x2i)
    x3.append(x3i)
    x4.append(x4i)
    x5.append(x5i)
    x6.append(x6i)
    y1.append(y1i)
    y2.append(y2i)
    y3.append(y3i)
    y4.append(y4i)
    y5.append(y5i)
    y6.append(y6i)
    vx1.append(vx1i)
    vx2.append(vx2i)
    vx3.append(vx3i)
    vx4.append(vx4i)
    vx5.append(vx5i)
    vx6.append(vx6i)
    vy1.append(vy1i)
    vy2.append(vy2i)
    vy3.append(vy3i)
    vy4.append(vy4i)
    vy5.append(vy5i)
    vy6.append(vy6i)
pl.xlim(0,6000)
pl.ylim(0,20000)
pl.xlabel('x/m')
pl.ylabel('y/m')
pl.title('trajectory of cannon shell no drag')
plot1,= pl.plot(x1,y1,'b')
plot2,= pl.plot(x2,y2,'g')
plot3,= pl.plot(x3,y3,'r')
plot4,= pl.plot(x4,y4,'c')
plot5,= pl.plot(x5,y5,'m')
plot6,= pl.plot(x6,y6,'y')
first_legend=pl.legend([plot1,plot2,plot3,plot4,plot5,plot6],['45deg','30deg','35deg','40deg','50deg','55deg'],loc="best")
pl.show()