#  MATH MODULES

#1.- MATH.CEIL(X)       return the ceiling of x the smallest integer greater than/equal to x....
import math
x=12.4
print(math.ceil(x))     #output-13...it always return greater value

#2.-MATH.FABS(X)        return the absolute value..it always return positive value
x=-12
print(math.fabs(x))

#3.-MATH.FACTORIAL(X)   return value error if x is not integral or negative
x=5                     #5*4*3*2*1=120 (return)
print(math.factorial(x))

#4.-MATH.FLOOR(X)       return the floor of x, the largest less than or equal to x.
x=12.4
print(math.floor(x))

#5.-MATH.FSUM(ITERABLE)   return an accurate floatingpoint sum of values in the iterable
l=[12,23,54,34]
print(math.fsum(l))

#6.-MATH.SQRT(X)         return the squareroot of x
x=4
print(math.sqrt(x))




