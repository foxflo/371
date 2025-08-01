#HW1 code template

# comments are any statements preceded by a pound sign
# they are very helpful for other people to understand your code, and are ignored by the computer
# I'll include comments to help you learn the basics of python

# import statements allow you to use other people's code in the form of packages
# you should never import something that trivializes the assignment
# if you're uncertain about whether you can use a package or not, feel free to ask

# matplotlib is a plotting library that has many useful functions for generating graphs
# you can look up helpful documentation for this online
# I'll leave it commented for now, so we won't generate plots
import matplotlib.pyplot as plt

# python's built-in math package contains many useful mathematical functions, constants, etc
from math import exp, log

# for loops are one of the fundamental code structures
# they allow you to repeat an action many times without having to perform it manually
# for example, we'll use it to generate a list of h values to test in numerical differentiation

# we initialize a bunch of empty lists to hold our values
h_values = []
derivative_values = []
errors = []
log_h_values = []
log_errors = []

# this is the syntax for a for loop
# range(100) generates the numbers 0 through 99 for you
# this for loop means execute the code inside with the values i=0, i=1, ..., i=99
# certain blocks of code need to be indented
# any code you want to execute within a for loop need to be indented inside that for loop
for i in range(100):
    # we will test h being negative powers of 2
    # ** is the exponentiation operator in python; be careful not to confuse this with ^
    h = 2**(-i)
    
    # our numerical differentiation rule is (f(x+h)-f(x)) / h
    # to use the example f(x) = e^x, we use the function exp we imported above
    # and we will approximate the derivative at x=1
    derivative = (exp(1+h)-exp(1))/h

    # the error is the difference between the actual value f'(1) = e and the value we computed
    # we use abs to compute the absolute value
    error = abs(derivative - exp(1))

    # compute the logs of h and the corresponding error
    log_h = log(h)
    log_error = log(error)

    # this code appends (adds to the end of the list) the value of the argument 
    h_values.append(h)
    derivative_values.append(derivative)
    errors.append(error)
    log_h_values.append(log_h)
    log_errors.append(log_error)
    
# now we've exited the for loop, so any code below is not part of the for loop
# we can also use list comprehensions (they are just abbreviated for loops) to achieve the same effect
h_values = [2**(-i) for i in range(100)]
derivative_values = [(exp(1+h)-exp(1))/h for h in h_values]
errors = [abs(derivative-exp(1)) for derivative in derivative_values]
log_h_values = [log(h) for h in h_values]
log_errors = [log(error) for error in errors]

# this is a very useful function for plotting
# there are many ways to modify it, but the basic usage is plt.plot(x,y)
# this graphs y (the second input) as a function of x (the first input)
plt.plot(h_values, errors)

# this code saves yout plot as the file "error vs h.png" so you can look at it later
# plt.savefig("error vs h")

# this code displays what you have plotted and clears the plot for the next graph
plt.show()


# it's a bit difficult to interpret the previous graph, so we plot the log scale
plt.plot(log_h_values, log_errors)
# plt.savefig("logerror vs logh")
plt.show()
