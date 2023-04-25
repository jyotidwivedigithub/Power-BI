#Numpy("Numerical Python")..is the fundamental package for scientific computing in python..
# it is a library that proides a multidimensional array object various derived object
#Array- is agrid of value and it contains information about the raw data how to locate an element &how to interpret an element.
#   1.-1D array    2.-2D array    3.-3D array...also make-High Dimensional Array
#Advantage of n=NumPy Array..consume less memory..fast as compared to python list..convenient to use.
#tools and technique to solve matematial problems...It is written in C and Python

#Create NumPy Arrays
import numpy as np
x=np.array([1,3,2,4])
print(x)
print(type(x))

#l=[1,2,3,4]
#print(l)
#print(type(x))   return <class 'list'

#l = []                #taking input from user
#for i in range(1,9):
    #int_l = int(input("Enter :"))
    #l.append(int_l)
#print(np.array(l))

#1.-1D Array
ar1=np.array([1,2,3,4])
print(ar1)
print(type(ar1))
print(ar1.ndim)

#2.-2D Array
ar2=np.array([[1,2,3,4],[5,6,7,8,]])
print(ar2)
print(type(ar2))
print(ar2.ndim)

#3.-3D Array
ar3=np.array([[[1,2,3,4],[5,6,7,8],[2,4,6,3]]])
print(ar3)
print(type(ar3))
print(ar3.ndim)






