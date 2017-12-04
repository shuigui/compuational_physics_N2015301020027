import pylab as pl
import math
'木星公转周期11.86yr  半径5.2AU mj/ms=0.000955 火星公转周期1.88yr 半径1.52AU mm/ms=     3.32*10^-7'
xm=[1.52]
ym=[0]
vmx=[0]
vmy=[2*math.pi*1.52/1.88]
xj=[5.2]
yj=[0]
vjx=[0]
vjy=[2*math.pi*5.2/11.86]
dt=0.001
x=0.001
for i in range(0,3000):
    rmi=(xm[i]**2+ym[i]**2)**(1/2)
    rji=(xj[i]**2+yj[i]**2)**(1/2)
    rmj=((xm[i]-xj[i])**2+(ym[i]**2-yj[i]**2))**(1/2)
    vmxi=vmx[i]-4*math.pi**2*xm[i]*dt/rmi**3-4*math.pi**2*x*(xm[i]-xj[i])*dt/rmj**3
    vmyi=vmy[i]-4*math.pi**2*ym[i]*dt/rmi**3-4*math.pi**2*x*(ym[i]-yj[i])*dt/rmj**3
    vmx.append(vmxi)
    vmy.append(vmyi)
    vjxi=vjx[i]-4*math.pi**2*xj[i]*dt/rji**3-4*math.pi**2*3.32*10**(-7)*(xj[i]-xm[i])*dt/rmj**3
    vjyi=vjy[i]-4*math.pi**2*yj[i]*dt/rji**3-4*math.pi**2*3.32*10**(-7)*(yj[i]-ym[i])*dt/rmj**3
    vjx.append(vjxi)
    vjy.append(vjyi)
    xmi=xm[i]+vmx[i+1]*dt
    ymi=ym[i]+vmy[i+1]*dt
    xm.append(xmi)
    ym.append(ymi)
    xji=xj[i]+vjx[i+1]*dt
    yji=yj[i]+vjy[i+1]*dt
    xj.append(xji)
    yj.append(yji)

ax = pl.gca()
ax.set_aspect(1)
pl1=pl.scatter(xm,ym,s=1)
pl2=pl.scatter(xj,yj,s=1)
pl.xlabel('AU')
pl.ylabel('AU')
pl.legend((pl1,pl2),('Mars','Jupiter'),loc='best')
pl.show()                 