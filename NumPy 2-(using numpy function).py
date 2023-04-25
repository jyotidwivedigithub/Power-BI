#Create NumPy Array using NumPy Functions...
#Spacial NumPy Array
 
# 1.-Array filled with 0's
import numpy as np
ar_zero=np.zeros(4)
print(ar_zero)
ar_zero=np.zeros((3,4))
print(ar_zero)

# 2.-Array filled with ones
ar_one=np.ones(5)
print(ar_one)
ar_one=np.ones((3,4))
print(ar_one)

# 3.-Create an empty array
ar_empty=np.empty(4)
print(ar_empty)
ar_empty=np.empty((3,4))
print(ar_empty)

# 4.-An array with a range of elements
ar_range=np.arange(4)
print(ar_range)
ar_range=np.arange((6))
print(ar_range)

# 5.-Array diagonal element filled with np.eye()
ar_dia=np.eye(5)
print(ar_dia)
ar_dia=np.eye((3))
print(ar_dia)

# 6.-Create an array with values that are spaced linearly in a specified interval
#Linspace
ar_lin=np.linspace(0,10, num=5)
print(ar_lin)