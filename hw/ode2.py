import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from math import sqrt

# initial value problem is
# y' = f(t,y)
# a <= t <= b
# y(a) = y0
# h is the initial timestep size -- this is often difficult to select properly
# tol is the error tolerance for each update step
def dopri5(a,b,y0,f,h,tol):
    trajectory = [y0]
    w = y0
    t = a
    accepted = 0
    rejected = 0
    fsal = f(t,w)
    while t < b:
        # in principle, we should compute k1=f(t,w) at each step
        # k1 = f(t,w)
        # however, this method has the "first same as last (fsal) property"
        # meaning that the last step (k7 in this case) of one round
        # is the same as the first step (k1) of the next round
        k2 = f(t+h/5, w+h/5*fsal)
        k3 = f(t+3*h/10, w + 3*h/40*fsal + 9*h/40*k2)
        k4 = f(t+4*h/5, w + 44*h/45*fsal - 56*h/15*k2 + 32*h/9*k3)
        k5 = f(t+8*h/9, w + 19372*h/6561*fsal - 25360*h/2187*k2 + 64448*h/6561*k3 - 212*h/729*k4)
        k6 = f(t+h, w + 9017*h/3168*fsal - 355*h/33*k2 + 46732*h/5247*k3 + 49*h/176*k4 - 5103*h/18656*k5)
        # the rows for k7 and w^5 in the butcher array are repeated
        # so we compute the w^5 step first to save some computation
        w5 = w + 35*h/384*fsal + 500*h/1113*k3 + 125*h/192*k4 - 2187*h/6784*k5 + 11*h/84*k6
        k7 = f(t+h, w5)
        w4 = w + 5179*h/57600*fsal + 7571*h/16695*k3 + 393*h/640*k4 - 92097*h/339200*k5 + 187*h/2100*k6 + h/40*k7
        err = sqrt(sum((w5-w4)**2)/len(w))/tol
        if err <= 1:
            accepted += 1
            # now we are done with k1, so we can overwrite it
            fsal = k7
            w = w5
            t+= h
            trajectory.append(w)
        else:
            rejected+=1
        if err == 0:
            h *= 5
        else:
            h *= min(5, max(.2, .8*(1/err)**(1/5)))    
    print("accepted=",accepted,"rejected=",rejected)
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

def pc3(a,b,y0,f,n):
    trajectory = [y0]
    w = y0
    h = (b-a)/n
    initial_onestep = rk4(a,a+2*h,y0,f,2)
    last3 = []
    for i in range(3):
        last3.append(f(a+i*h,initial_onestep[i]))

    t = a+2*h
    for i in range(n):
        w_pred = w + h*(23/12*last3[-1] - 4/3*last3[-2] + 5/12*last3[-3])
        w = w + h*(9/24*f(t+h,w_pred) + 19/24*last3[-1] - 5/24*last3[-2] + 1/24*last3[-3])
        #print(sqrt(sum((w-w_pred)**2)))
        trajectory.append(w)
        last3.append(f(t+h,w))
        del last3[0]
        t += h
    return trajectory
        
# orbit problem from previous homework
c=0.012277471
d=1-c
def orbit(t,y):
    f0 = y[1]
    f1 = y[0] + 2*y[3] - d*(y[0]+c)/((y[0]+c)**2+y[2]**2)**(3/2) - c*(y[0]-d)/((y[0]-d)**2 + y[2]**2)**(3/2) 
    f2 = y[3]
    f3 = y[2] - 2*y[1] - d*y[2]/((y[0]+c)**2 + y[2]**2)**(3/2) - c*y[2]/((y[0]-d)**2 + y[2]**2)**(3/2)
    return np.array([f0,f1,f2,f3])

y0 = np.array([.994, 0, 0, -2.00158510637908])
a = 0
b = 17.06521656015796
# adaptive orbit testing
import time
start = time.time()
temp = dopri5(a,b,y0,orbit, 10**-1, 10**-6)
end = time.time()
print("DOPRI5 runtime:", end-start)
x = [t[0] for t in temp]
y = [t[2] for t in temp]
plt.plot(x,y, label="dopri5")
plt.legend()
plt.show()

# predictor-corrector orbit testing
import time
start = time.time()
temp = pc3(a,b,y0,orbit,40000)
end = time.time()
print("pc3 runtime:", end-start)
x = [t[0] for t in temp]
y = [t[2] for t in temp]
plt.plot(x,y, label="pc3")
plt.legend()
plt.show()
