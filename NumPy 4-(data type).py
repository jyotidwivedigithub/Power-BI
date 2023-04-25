#Integer
import numpy as np
var=np.array([1,2,3,4,5])
print("Data Type : ",var.dtype)

#Float
import numpy as np
var1=np.array([1.2,3.4,4.5,5.5])
print("Data Type : ",var1.dtype)

#String
import numpy as np
var2=np.array(["a","b","c"])
print("Data Type : ",var2.dtype)

var3=np.array(["a","b","c",2,4,3])
print("Data Type : ",var3.dtype)

#List of characters that used to represent dtype in NumPy..
  # i=integer,  b=boolean,   u=unsigned integer,  f=float,   c=complex float,   m=timedelta,
  # M=datetime, O=object,    S=sting,  U=Unicode string,  V=the fixed chunk of memory for other types (void)
 #convert datatype

x=np.array([1,2,3,4],dtype=np.int8)   #integer
print(x)
print("Data Type : ",x.dtype)

x1=np.array([1,2,3,4],dtype="f")      #float
print(x)
print("Data Type : ",x1.dtype)

x2=np.array([1,2,3,4])
new=np.float32(x2)
new_one=np.int_(new)
print("Data Type : ",x2.dtype)
print("Data Type : ",new.dtype)
print("Data Type : ",new_one.dtype)
print(x2)
print(new)
print(new_one)


x3=np.array([4,6,8,2])
new1=x3.astype(float)
print(x3)
print(new1)
