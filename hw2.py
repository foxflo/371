#hw2 code template

# to define your own functions, use the "def" keyword
# this defines a function called bisect which takes four inputs: func, a, b, err
# func is the function to find a root of
# a and b are the left and right endpoints of the interval where you are looking for a root
# err is the desired tolerance to use for the stopping criterion
# be careful with the choice of err, your code may run forever if don't choose reasonable tolerances
def bisect(func, a, b, err):
    error = None
    # your code here
    # feel free to take inspiration from class
    # the return keyword tells your function to finish execution
    # and output whatever value is after the return
    # in this case, we'll return a pair (a, error) consisting of the
    # approximation and a bound on its error
    # feel free to modify this line if you named it something else
    return (a, error)


# import the logarithm function from the builtin math package in python
# note that "log" in python implicitly means natural log
from math import log
# this defines the function from problem 2.2
def f(x):
    return (1/x) + log(x) - 2

# now you can test a few values of your function
print("f(10) =",f(10))

# choose your desired values of a and b
a = 1
b = 2000
err = 100
print("approximate root of f(x) found by bisection:", bisect(f, a, b, err))
