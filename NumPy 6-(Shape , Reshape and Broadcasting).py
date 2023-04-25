#   Shape
import numpy as np
var=np.array([[1,2,3,4],[2,3,4,5]])
print(var)
print(var.shape)
print(var.ndim)

var1=np.array([2,4,6,8],ndmin=4)
print(var1)
print(var1.shape)
print(var1.ndim)

#   Reshape
var2=np.array([1,2,3,4,5,6,7,8,9])
print(var2)
print(var2.ndim)
x=var2.reshape(3,3)              # 2-Dimensionsl
print(x)
print(x.ndim)

var3=np.array([1,2,3,4,5,6,7,8])
print(var3)
print(var3.ndim)
x1=var3.reshape(2,2,2)            # 3-Dimensional
print(x1)
print(x1.ndim)

print()                           #again reshpe 3D to 1D
one=x1.reshape(-1)                #(-1) is used to return in 1D
print(one)
print(one.ndim)



## BROADCASTING ARRAy work when...1.-same dimension  2.-match atleast 1 dimension 
import numpy as np
var=np.array([1,2,3])
print(var.shape)
print(var)

var1=np.array([[1],[2],[3]])
print(var1.shape)
print(var1)
print()

print(var+var1)              #addition


x=np.array([[1],[2]])
print(x.shape)

y=np.array([[1,2,3],[3,5,4]])
print(y.shape)

print(x+y)










