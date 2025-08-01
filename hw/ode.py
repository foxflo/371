import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

# initial value problem is
# y' = f(t,y)
# a <= t <= b
# y(a) = y0
# n is number of steps to take, so h = (b-a)/n
def euler(a,b,y0,f,n):
    trajectory = [y0]
    w = y0
    h = (b-a)/n
    t = a
    for i in range(n):
        # note that the result of f is a numpy array, and w is a numpy array
        # so the operations in the line below behave like they would for vectors
        w = w + h*f(t,w) 
        trajectory.append(w)
        t += h
    return trajectory

def rk4(a,b,y0,f,n):
    trajectory = [y0]
    w = y0
    h = (b-a)/n
    t = a
    for i in range(n):
        k1 = f(t,w)
        k2 = f(t+h/2, w+h/2*k1)
        k3 = f(t+h/2, w+h/2*k2)
        k4 = f(t+h, w+h*k3)
        w = w + h/6*(k1+2*k2+2*k3+k4)
        trajectory.append(w)
        t += h
    return trajectory

def vanderpol(t,y, mu=2):
    return np.array([y[1], mu*(1-y[0]**2)*y[1] - y[0]])

c=0.012277471
d=1-c
def orbit(t,y):
    f0 = y[1]
    f1 = y[0] + 2*y[3] - d*(y[0]+c)/((y[0]+c)**2+y[2]**2)**(3/2) - c*(y[0]-d)/((y[0]-d)**2 + y[2]**2)**(3/2) 
    f2 = y[3]
    f3 = y[2] - 2*y[1] - d*y[2]/((y[0]+c)**2 + y[2]**2)**(3/2) - c*y[2]/((y[0]-d)**2 + y[2]**2)**(3/2)
    return np.array([f0,f1,f2,f3])

def curvature(t,y):
    return np.array([y[1],-y[0]*(1+y[1]**2)**(3/2)])

#vanderpol testing for 3.1
a = 0
b = 20
y0 = np.array([0,1])
approx = euler(a,b,y0,vanderpol,250)
x,y = zip(*approx)
plt.plot(x,y, label="starting (0,1)")
plt.show()

y0 = np.array([1,0])
approx = euler(a,b,y0,vanderpol,1000)
x,y = zip(*approx)
plt.plot(x,y, label="starting (1,0)")

y0 = np.array([3,3])
approx = euler(a,b,y0,vanderpol,1000)
x,y = zip(*approx)
plt.plot(x,y, label="starting (3,3)")
plt.legend()
plt.show()

#orbit testing for 3.2
y0 = np.array([.994, 0, 0, -2.00158510637908252240537862224])
a = 0
b = 17.0652165601579625588917206249
errs = []
for i in range(1, 101):
    #temp = euler(a,b,y0,orbit,10000*i)
    temp = rk4(a,b,y0,orbit,100*i)
    errs.append(sqrt((temp[-1][0]-.994)**2+temp[-1][2]**2+temp[-1][1]**2 + (temp[-1][-1]+2.00158510637908252240537862224)**2))
x,_,y,_ = zip(*temp)
plt.plot(x,y)
plt.show()

N = np.array(range(1,101))
plt.plot(N,errs)
plt.show()

plt.plot(np.log(100*N), np.log(np.array(errs)))
plt.show()

#3.3 curvature testing
a=0
b=20
n=1000
y0=np.array([0,sqrt(3)])
approx = rk4(a,b,y0,curvature,n)
y,yp = zip(*approx)
x=np.arange(a,b+1/n,(b-a)/n)
plt.plot(x,y)
plt.show()
