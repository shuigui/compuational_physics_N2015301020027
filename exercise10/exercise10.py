import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
v0=np.zeros((100,100))
for i in range(45,55):
    for j in range(45,55):
        v0[i][j]=1
v=v0
for k in range(0,300):
    for i in range(1,99):
        for j in range(1,99):
            if v0[i][j]!=1:
                v[i,j]=(v0[i-1,j]+v0[i+1,j]+v0[i,j-1]+v0[i,j+1])/4
    for i in range(1,99):
        for j in range(1,99):
            if v[i][j]!=1:
                v0[i,j]=(v[i-1,j]+v[i+1,j]+v[i,j-1]+v[i,j+1])/4
x=np.linspace(-1,1,100)
y=np.linspace(-1,1,100)
X, Y = np.meshgrid(x, y)

pl.contour(X,Y,v0, colors = 'black')
pl.show()

u,w=np.gradient(-v0)
pl.quiver(X, Y, w, u)
pl.show()

ax=pl.subplot(111,projection='3d')
ax.scatter(X, Y, v0, s=1)
pl.show()

                
