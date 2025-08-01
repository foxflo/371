# bisection
# we start with the left endpoint a=1 and right endpoint b=2
# since we know the square root of 3 is between 1 and 2
a = 1
b = 2
# we'll count how many steps we took using this counter variable
counter = 0

# there are two main types of iteration in python, for loops and while loops
# for loops are useful when you know how many times you want to repeat an action
# while loops are useful when you want to run something until some condition is met
# in this case, the code inside the while loop will execute as long as the length
# of the interval [a,b] is larger than 2^(-52)
while b-a > 2**-52:
    # compute the midpoint of the interval [a,b]
    mid = (a+b)/2
    # increment the counter by 1, this could also be written as counter = counter + 1
    counter += 1
    # if-elif-else statements are another very useful to change the behavior
    # depending on what condition is satisfied
    # if statements can have as many elif statements as you like, but only one if and only one else
    # if the midpoint is larger than the square root of 3, then decrease the right endpoint
    if mid**2-3>0:
        b = mid
    # else if the midpoint is smaller than the square root of 3, then increase the left endpoint
    elif mid**2-3<0:
        a = mid
    # else if we got lucky and found the square root of 3, then we can stop immediately
    else:
        a = mid
        b = mid
        break

# the print function allows you to print out output of your code when running
# the quoted type is a string
print("Bisection to find square root of 3 as solution to x^2-3 = 0")
# you can print multiple things at once -- note that counter is an integer here, so print can also handle numeric types
print(counter, "bisection took iterations to converge")
print(a, "approximate square root of 3 using bisection")
print(3**.5, "computed square root of 3 using arithmetic")


# fixed point iteration
# we start with the guess a=1.5
a = 1.5
counter = 0
# we will keep going until the error is smaller than 2^(-49)
# the error of floating point is slightly larger than the error of bisection
while abs(a**2-3)>2**-49:
    counter += 1
    # we try several different fixed point formulas -- which one seems to perform the best?
    #a = 3/a
    #a = a - (a**2-3)
    #a = a - (a**2-3)/2
    a = a - (a**2-3)/(2*a)
