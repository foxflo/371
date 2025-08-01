import numpy as np

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

def multistep(a,b,y0,f,n):
    trajectory = [y0]
    y1 = rk4(a,a+(b-a)/n,y0,f,1000)
    trajectory.append(y1[-1])
    prev_w = y0
    w = y1[-1]
    h = (b-a)/n
    t = a+h
    for i in range(n-1):
        # note that the result of f is a numpy array, and w is a numpy array
        # so the operations in the line below behave like they would for vectors
        wexp = w + h*(3/2*f(t,w)-1/2*f(t-h,prev_w))
        wimp = w + h*(5/12*f(t+h,wexp)+ 8/12*f(t,w) - 1/12*f(t-h,prev_w))
        trajectory.append(wimp)
        prev_w = w
        w = wimp
        t += h
    return trajectory

def test(x,y):
    return np.array([y[1], (1/8)*(32+2*x**3-y[0]*y[1])])

y0 = np.array([17,-10])
print(multistep(1,1.5,y0,test,5))
y0 = np.array([17,-18])
print(multistep(1,1.5,y0,test,5))
y0 = np.array([17,-14])
print(multistep(1,1.5,y0,test,5))
print(155/12)
