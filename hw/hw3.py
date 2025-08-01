# hw3 code template

# in principle, we should take advantage of previous computations to save time later
# however, for simplicity here, we will recompute the divided differences as we need them
#
# func represents the function to evaluate
# pts is a list [x1,...,xk] of points at which we want to compute the divided difference
# this function returns the divided difference f[x1,...,xk]
def div_diff(func, pts):
    # if there is only one interpolation point, then the divided difference is the function value
    if len(pts) == 1:
        return func(pts[0])

    # otherwise, we'll recursively compute the divided differences
    # to access elements of a list x, we use the bracket notation x[i] to access the ith element of the list
    # note that list indices start counting from 0 in python, so x[0] refers to the first element of x
    # negative list indices start counting from the end, so x[-1] refers to the last element of x
    # the colon in x[a:b] means to take the elements from index a until index b (not including b)
    # if the first index is omitted, then it refers to the start of the list
    # if the last index is omitted, then it refers to the end of the list
    # for example, x[1:] means take every element in x except the 0th element.
    # x[:-1] means take every element in x except the last element 
    return (div_diff(func, pts[1:]) - div_diff(func, pts[:-1])) / (pts[-1] - pts[0])

# using the divided difference function above (or you can feel free to improve it if you like!)
# implement Newton interpolation
#
# the input func represents the function to interpolate
# interp_pts is a list (or whatever you see fit to use) of interpolation points
def newton(func, interp_pts):
    # YOUR CODE HERE

# this function takes an interval [a,b] and an integer n and creates n evenly spaced points in [a,b]
def equispaced(a,b,n):
    return [a+(b-a)*i/(n-1) for i in range(n)]

# this function takes an interval [a,b] and an integer n and creates n Chebyshev points in [a,b]
def chebyshev(a,b,n):
    # YOUR CODE HERE

def f(x):
    return 1/(1+x**6)

