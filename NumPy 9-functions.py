# 1-Joining Array[np.concatenate()]..means putting contents of 2 or more array in singlr array.
      # we can also use stack function for merging/joining
import numpy as np
var=np.array([1,2,3])            # 1-D
var1=np.array([4,5,6])
ar=np.concatenate((var,var1))    #merge along with row
ar1=np.stack((var,var1),axis=1)         #merge along with column(axis=1)
print(ar)
print(ar1)
ar_new=np.hstack((var,var1))     #h=merge along with row
ar_new1=np.vstack((var,var1))    #v=merge along with column
ar_new2=np.dstack((var,var1))    #d=hight
print(ar_new)
print(ar_new1)
print(ar_new2)
print()

vr=([[1,2],[4,5]])               # 2-D
vr1=([[3,4],[7,6]])
ar=np.concatenate((vr,vr1))
print(ar)
ar_new=np.concatenate((vr,vr1),axis=1)        #according to row
print(vr)
print(vr1)
print(ar_new)
ar_new1=np.concatenate((vr,vr1),axis=0)        #according to column
print(ar_new1)
print()

# 2-Split Array
import numpy as np
var=np.array([1,2,3,4,5,6])      #1-D
print(var)
ar=np.array_split(var,3)
print(ar)
print(type(ar))
print(ar[0])
print()

var1=np.array([[1,2,3,4],[6,5,4,3]])   #2-D
print(var1)
ar1=np.array_split(var1,3,axis=1)
print(ar1)
print(type(ar1))

# 3-Search Array[np.where()]...search any array for a certain value,& return indexes that get match.
var=np.array([1,2,3,4,5,6])
x=np.where(var ==1)
print(x)
x1=np.where((var%2)==0)            #it givex index no divided by 2 and give remainder 0
print(x1)

# 4-Search Sorted Array..which performs a binary search in the array,and returns the index where the speified value would be inserted ro maintain the search order.
var1=np.array([1,2,3,4,6])
x1=np.searchsorted(var1,5)     #return index where the value place
print(x1)
print(np.searchsorted(var1,5,side="right"))

x2=np.searchsorted(var1,[5,6],side="right") 
print(x2)

# 4-Sort Array
var_1=np.array([1,5,8,7,3,4,11,54,46,78])
print(np.sort(var_1))                     #array will sort in acending order

var_2=np.array(['a','s','d','e'])
print(np.sort(var_2))

# 5-Filter Array..getting some elements out of an existing array and creating a new array out of them.
var_2=np.array([1,5,8,7])
f=[True,False,False,True]
new_a=var_2[f]
print(new_a) 
print(type(new_a))
#print(var_2[f])

#...ARITHMETIC FUNCTION...
 # 1-Shuffle...change the sequence of data
var=np.array([1,5,8,7])
np.random.shuffle(var)
print(var)

 # 2-Unique...for getting unique data
var=np.array([1,2,3,4,3,3,5,6,7,8,])
x=np.unique(var)
print(x)
print()
x1=np.unique(var,return_index=True)  #data with index no.
print(x1)
print()
x2=np.unique(var,return_index=True,return_counts=True)
print(x2)

 # 3-Resize..for resizing array
var1=np.array([1,2,3,4,5,6,7,8,])
y=np.resize(var1,(2,4))       #2-row,4-colunm
print(y)
x=np.resize(var1,(4,2))       #4-row,2-column
print(x)

 # 4-Flatten...convert 2-dimension array in 1-dimension
var1=np.array([1,2,3,4,5,6,7,8,])
y=np.resize(var1,(2,4))
print(y)
print(y.flatten())
print(y.flatten(order="f"))
print(y.flatten(order="c"))
print("Flatten: ",y.flatten(order='f'))
 
 # 5-Ravel...convert 2-dimension array in 1-dimension
print("Ravel: ",np.ravel(y))
print("Ravel: ",np.ravel(y,order='f'))
print("Ravel: ",np.ravel(y,order='k'))

# NOTES...Orders:{'C','F','A','K'},Optional
  #"C" means to flatten in row-major (C-style)order
  #"F" means to flatten in column-major (Fortran-style)order
  #"A" means to flatten in column-major order if `a` is Fortan *contiguous* in memory,row-major order otherwise.
  #"K"means to flatten `a` in the order the elements occur in memory.
  #The default is "C"

# INSERT Function...also use APPEND function
var=np.array([1,2,3,4,5])
print(var)
v=np.insert(var,2,42)         #here 2-position,42-data to insert after 2
#v=np.append(var,2.5) 
print(v)
print(type(v))
v1=np.insert(var,(2,3),(3.5)) 
print(v1)

var=np.array([[1,2,3,4],[5,6,8,7]])
x=np.insert(var,2,[4,3],axis=1)    #1-column
print(x)

var2=np.array([[1,2,3],[4,6,5]])
#x1=np.insert(var2,2,[4,3,6],axis=0) #0-row
x1=np.append(var2,[[4,3,6]],axis=0)
print(x1)

# DELETE Function
var=np.array([1,2,3,4,5])
d=np.delete(var,1)             #here 1 is index no.
print(d)






