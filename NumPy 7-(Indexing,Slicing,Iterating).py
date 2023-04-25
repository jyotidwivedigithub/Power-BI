# INDEXING
import numpy as np
var=np.array([1,2,3,4])
print(var[2])
print(var[-3])

var1=np.array([[2,4],[4,6]])
print(var1)
print()
print(var1[1,1])

var2=np.array([[[2,3,4],[4,3,2]]])
print(var2)
print()
print(var2[0,1,2])

#SLICING.....#print(start:stop:step)
var3=np.array([1,2,3,4,5,6,7])           # 1-Dimension
              #0,1,2,3,4,5,6
print(var3)
print()
print("2 to 5: ",var3[1:5])
print("start to end: ",var3[0:6:2])
print("1 to end: ",var3[1:])
print("start to 6: ",var3[ :6])
print("stop: ",var3[1:6:2])
print()

var4=np.array([[1,2,3,4],[5,6,7,8],[12,13,14,15]])   # 2-Dimension
print(var4)
print()
print("5 to 8",var4[1,0:])
print("12 to 15",var4[2,1:3])

var5=np.array([[[1,2,3,4],[3,4,1,5],[11,12,13,14]]])         # 3-Dimension
print(var5[:,:,0:])
print(var5[:,:,1:])
print(var5[:,:,2:])
print(var5[:,:,3:])


#Iteration....use  np.nditer() for iteration,  np.ndenumerate() for iteration with indixing
import numpy as np
x=np.array([1,2,3,4,5])           # 1-Dimension Iteration
for i in x:
    print(i)
#for i in np.nditer(x):
#  print(i)

x1=np.array([[1,2,3,4],[5,4,3,2]])  # 2-Dimension Iteration
print(x1)
print()
for k in x1:
    for l in k:
        print(l)
#for k in np.nditer(x1):
#  print(k)

x2=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  # 3-Dimension Iteration
print(x2)
print()
for i in x2:
    for j in i:
        for k in j:
            print(k)
#for i in np.nditer(x2):
#  print(i)
print()
for i in np.ndenumerate(x2):        #np.indenumerate for iteration with idex no.
    print(i)




