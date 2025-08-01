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

# stiff equation testing
# run newton iterations to solve the implicit Euler step
# w(t_i+1) = w(t_i) + hf(t_i+1, w_i+1)
# we'll assume here that the derivative fprime of f is given as input
# however, in general it will not be available and we will need to use
# modifications of Newton's method which don't require explicit knowledge of the derivative
def fp(f,fprime,t,w,h, tol=2**-40):
    error = 1
    prev_w = w
    #use the difference between the two iterations as an approximation for the error
    while error > 2**-40:
        next_w = w-(w-(prev_w + h*f(t,w)))/(1-h*fprime(t,w))
        error = abs(w-next_w)
        w = next_w
    return w

def implicit_euler(a,b,y0,f,fprime,n):
    trajectory = [y0]
    w = y0
    h = (b-a)/n
    t = a
    for i in range(n):
        # solve the implicit euler step using Newton iterations
        w = fp(f,fprime,t+h,w,h)
        trajectory.append(w)
        t += h
    return trajectory

def stiff(t,y):
    return 50*(cos(t)-y)

# this is the derivative for Newton's method in fixed point iteration
# be careful about which derivative to take...
def stiff_prime(t,y):
    return -50

# stiff testing
import matplotlib.pyplot as plt
from math import sin, cos, exp
y0 = 0
fine = [i/100 for i in range(101)]
exact = [50*(sin(t)+50*cos(t)-50*exp(-50*t))/2501 for t in fine]
plt.plot(fine,exact, label="exact solution")

for n in [1000]:#range(5,31,5):
    #temp = implicit_euler(0,1,y0,stiff,stiff_prime,n)
    temp = euler(0,1,y0,stiff,n)
    #temp = rk4(0,1,y0,stiff,n)
    times = [1/n*i for i in range(n+1)]
    plt.plot(times,temp, label="rk4_"+str(n))

plt.legend()
plt.show()
