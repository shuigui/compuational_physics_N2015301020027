import pylab as pl
import math as math
m=1
q=0.5
l=9.8
g=9.8
ΩD=2/3
dt=0.04

def f(FD):
    t = [0]
    w = [0]
    b = [0.2]
    E = [m*g*l*(1-math.cos(b[0]))]
    for i in range(1,1500):
        wi = w[i-1]-((g/l)*math.sin(b[i-1])+q*w[i-1] - FD*math.sin(ΩD*t[i-1]))*dt
        w.append(wi)
        bi = b[i-1] + w[i]*dt
        if bi > math.pi :
            bi = bi-2*math.pi
        elif bi < -math.pi:
            bi = bi + 2*math.pi
        else:
            bi = bi
        b.append(bi)
        ti = t[i-1] + dt
        t.append(ti)
        Ei = 1/2*m*l*w[i]**2 + m*g*l*(1-math.cos(b[i]))
        E.append(Ei)
    return[t,w,b,E]

pl.subplot(311)
pl.title("FD=0.5")
pl.plot(f(0.5)[0],f(0.5)[3])

pl.subplot(312)
pl.title("FD=1.2")
pl.plot(f(1.2)[0],f(1.2)[3])

pl.subplot(313)
pl.title("FD=0")
pl.plot(f(0)[0],f(0)[3])

pl.suptitle('E versus t')
pl.xlabel('E（j)')
pl.ylabel('t（s)')
pl.show()






     
     
     
     
     
     
     
     
     
     
     
     
 
