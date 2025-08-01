# feel free to import any math functions you need
from math import sqrt
from math import sin,log
import numpy as np

# these are the integration points for 5-point Gaussian integration on [-1,1]
roots = [-1/3*sqrt(2*sqrt(10/7) + 5),  -sqrt(-2/9*sqrt(10/7) + 5/9), 0, sqrt(-2/9*sqrt(10/7) + 5/9), 1/3*sqrt(2*sqrt(10/7) + 5)]
#roots = [-.906,-.538,0,.538,.906]

# these are the weights for Gaussian integration on [-1,1]
weights = [21/50*(5*sqrt(10) + sqrt(7))/(7*sqrt(10) + 4*sqrt(7)), 21/50*(5*sqrt(10) - sqrt(7))/(7*sqrt(10) - 4*sqrt(7)), 128/225, 21/50*(5*sqrt(10) - sqrt(7))/(7*sqrt(10) - 4*sqrt(7)), 21/50*(5*sqrt(10) + sqrt(7))/(7*sqrt(10) + 4*sqrt(7))]
#weights = [0.2326,0.47897,0.5689,.47897,.2326]

# given an input point for Gaussian integration on [-1,1]
# output the corresponding point for Gaussian integration on [a,b]
def transform_pt(a,b,pt):
    return (b-a)/2 * pt + (a+b)/2

# given an input weight for Gaussian integration on [-1,1]
# output the corresponding weight for Gaussian integration on [a,b]
def transform_wt(a,b, wt):
    return (b-a)/2*wt

# implement 5 point gaussian integration
def gauss5(a,b, func):
    # first, transform the roots and weights from the interval [-1,1] to the interval [a,b]
    # then, evaluate func at the integration points and sum them with the correct weights
    pts = [transform_pt(a,b,root) for root in roots]
    wts = [transform_wt(a,b,weight) for weight in weights]
    evals = [func(pt) for pt in pts]
    return sum([w*p for (w,p) in zip(wts, evals)])

#print([gauss5(-1,1,lambda x:x**i) for i in range(10)])

def gadap(a,b,func,eps=2**-40, max_iter = 5000):
    working = [(a,b,gauss5(a,b,func))]
    done = []
    total = 0
    iters = 0
    fn_evals = 0
    while working:
        iters += 1
        if iters > max_iter:
            raise Exception("maximum iteration count reached without convergence")
        # get an element from the working list of in-progress intervals
        (curr_a, curr_b, curr_int) = working.pop()
        left_a = curr_a
        left_b = (curr_a+curr_b)/2
        left_int = gauss5(left_a,left_b,func)
        right_a = (curr_a+curr_b)/2
        right_b = curr_b
        right_int = gauss5(right_a,right_b,func)
        fn_evals += 10
        if abs(curr_int - (left_int + right_int)) > eps*max(abs(curr_int), abs(left_int+right_int)):
            working.append((left_a,left_b,left_int))
            working.append((right_a,right_b,right_int))
        else:
            total += left_int + right_int
            done.append((left_a,left_b,left_int))
            done.append((right_a,right_b,right_int))
    return total, done, fn_evals

for i in range(1,17):
    result = gadap(0,1,lambda x:x**(-x),10**(-i))
    #print output in LaTeX friendly format
    print("10^{-"+str(i)+"} & "+str(result[0])+"&"+str(result[2])+"\\\\")

def simpson(a,b,f,num):
    #produce points at which to evaluate functions
    #h=(b-a)/(num-1)
    #a, a+h, a+2h, ..., b=a+(num-1)*h
    interval = np.arange(a,b+2**-52,1/(num-1))
    #for every pair of points
    #(a,a+h,a+2h), then (a+2h, a+3h, a+4h), then (a+4h, a+5h, a+6h), etc...
    #composite simpson requires num function evaluations
    fevals = [f(x) for x in interval]
    total = 0
    for i in range(0,num-1,2):
        total += fevals[i] + 4*fevals[i+1] + fevals[i+2]
    return total*(b-a)/(num-1)/3

f = lambda x: x**(-x)
for i in range(101,1702,100):
    #print output in LaTeX friendly format
    print(" & "+str(simpson(0,1,lambda x:x**-x,i)) + " & "  + str(i)+"\\\\")
