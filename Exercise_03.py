import pylab as pl
g = 9.8
T = 10
dt =float(input('time_step'))
t=[0]
v = [0]
y = [0]
for i in range(1,int(T/dt)):
    vi =v[i-1] - g*dt
    ti = i * dt
    t.append(ti)
    # Correct kinematic equation: y = y0 + v0*t + 0.5*a*t^2
    # For free fall from rest: y = -0.5*g*t^2
    yi = -0.5 * g * t[i]**2
    v.append(vi)
    y.append(yi)
pl.title('time_step = '+ str(dt))
pl.xlabel('t')
pl.ylabel('v')
plot1, = pl.plot(t,y,'b')
plot2, = pl.plot(t,v,'go')
first_leend=pl.legend([plot1,plot2],['exact solution','Euler solution'],loc="best")
pl.show(t,y)
pl.show(t,v)