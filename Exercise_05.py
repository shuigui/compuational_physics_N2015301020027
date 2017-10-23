# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:45:46 2017

@author: panxiang
"""

import pylab as pl
import math
x = [0]
y = [3]
z = [0]
w = -2000/60*(math.pi/30)
v = 15
vx = [v*math.cos(math.pi/4)]
vy = [v*math.sin(math.pi/4)]
vz = [0]
dt = 0.001
g = -9.8
B2 = 0.0039
def f (a,b):
    return a + b*dt
for i in range(1,10000):
    vxi = f(vx[i-1],B2/0.15*v*vx[i-1])
    vx.append(vxi)
    xi = f(x[i-1],vx[i-1])
    x.append(xi)
    vyi = f(vy[i-1],g)
    vy.append(vyi)
    yi = y[i-1] + vy[i-1]*dt
    y.append(yi)
    vzi = f(vz[i-1],-0.00041*w*vx[i-1])
    vz.append(vzi)
    zi = f(z[i-1],vz[i-1])
    z.append(zi)

pl.xlim(0,60)
pl.ylim(0,10)
pl.xlabel('x/m')
pl.ylabel('y or z')
plot1,=pl.plot(x,y,'b')
plot2,=pl.plot(x,z,'r')
first_legend= pl.legend([plot1,plot2],['y','z'],loc='best')  
pl.show()
  
     
