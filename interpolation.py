import matplotlib.pyplot as plt
from math import cos, pi, log, sin, sqrt

# slow divided difference computation following recursive definition:
# f[x] = f(x)
# f[x1,...,xn] = (f[x2,...,xn]-f[x1,...,x(n-1)]) / (xn - x1)
# func is the function whose divided difference we want to evaluate
# pts is the list of points for which we want to compute the divided differences
# note that this implementation repeats many calculations since we don't
# store the results of previous recursive calls
# note that this implementation cannot handle repeated points
def div_diff(func, pts):
    if len(pts) == 1:
        return func(pts[0])
    return (div_diff(func, pts[1:]) - div_diff(func, pts[:-1])) / (pts[-1] - pts[0])

# a better divided differences computation which avoids repeating any computations
# and allows for a generalized interpration of divided differences using repeated points
# func is the function whose divided difference we want to evalute
# pts is the list of points for which we want to compute the divided differences
# deriv is an optional argument containing the derivative of the function func
# and is necessary in the case that pts contains repeated points
def div_diff(func,pts,deriv=None):
    out = []
    current = []
    for i in range(len(pts)):
        temp = [func(pts[i])]
        for j in range(i):
            if pts[i] == pts[i-1-j]:
                temp.append(deriv(pts[i]))
            else:
                temp.append((temp[-1]-current[j])/(pts[i]-pts[i-1-j]))
        current = temp
        out.append(current[-1])
    return out

# newton interpolation of a function func at the points pts
# pts can contain repeated points, in which case we will require the optional derivative argument
def newton(func, pts, deriv=None):
    div_diffs = div_diff(func, pts, deriv=deriv)
    def P(x):
        total = 0
        N_poly = 1
        for i in range(len(pts)):
            total += div_diffs[i]*N_poly
            N_poly *= (x-pts[i])
        return total
    return P

# return n equally spaced points in the interval [a,b]
def equispaced(a,b,n):
    return [a+(b-a)*i/(n-1) for i in range(n)]

# return the n Chebyshev points in the interval [a,b]
def chebyshev(a,b,n):
    return [(b-a)/2*cos(pi/(2*n) + i*pi/n)+a+(b-a)/2 for i in range(n)]

def f(x):
    return 1/(1+x**6)

num_pts = [4,6,10,18]
x_vals = [-2+4*i/1000 for i in range(1001)]
evals_f = [f(val) for val in x_vals]
plt.plot(x_vals, evals_f, label="original")
for i in num_pts:
    pol = newton(f,equispaced(-2,2,i))
    evals = [pol(val) for val in x_vals]
    plt.plot(x_vals,evals,label="n="+str(i-1))

plt.legend()
plt.title("Interpolation using equally spaced points")
#plt.savefig("poly_equispaced")
plt.show()

plt.plot(x_vals, evals_f, label="original")
for i in num_pts:
    pol = newton(f,chebyshev(-2,2,i))
    evals = [pol(val) for val in x_vals]
    plt.plot(x_vals, evals, label="n="+str(i-1))

plt.legend()
plt.title("Interpolation using Chebyshev points")
#plt.savefig("poly_cheby")
plt.show()
