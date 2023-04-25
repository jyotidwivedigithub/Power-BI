#  Create Matrix
import numpy as np
var=np.matrix([[1,2,3],[4,5,6]])
print(var)
print(type(var))

var1=np.array([[1,2,3],[4,5,6]])
print(var1)
print(type(var1))

#... ARITHMETIC OPERATION...
print(var+var1)              #Addition
print(var-var1)              #Subtraction

var2=np.matrix([[1,2],[4,5]])
var3=np.matrix([[1,2],[4,5]])
print()

#print(var2*var3)          *-it will not work in matrix,we use dot(.)for multipication in matrix.
print(var2.dot(var3))         # multiplication..(.dot)..var2=(2*2),var3=(2*2)


#...Matrix Function
  #Transpose(),Swapaxes(),Inverse(),Power(),Determinate()
var=np.matrix([[1,2,3],[5,6,7]])
print(var)
print()

 # 1-Transpose Function...convert row to column
print(np.transpose(var))
#print(var.T)           #shortcut for transpose
print()

 # 2-Swapaxes Function....convert row to column..vise-versa 
print(np.swapaxes(var,0,1))   #convert 0 axis in 1 axis
print()

var2=np.matrix([[1,2],[3,4]])
print(var2)
print()
print(np.swapaxes(var2,0,1))
print()

 # 3-Inverse Function....(np.linalg.inv( ))
var3=np.matrix([[1,2],[3,4]])
print(var3)
print()
print(np.linalg.inv(var3))
print()

 # 4-Power Function..(dot.)..(np.linalg.matrix_power(var,n))..condition of n can be n=0,n>0,n<0
    #n=0...Identity Matrix=[1 0/0 1]
    #n>0...power(multiplication)
    #n<0...Inverse*Power
var4=np.matrix([[1,2],[3,4]])
print(var4)
print()

print(np.linalg.matrix_power(var4,2))   #matrix multiplied by 2
print()
print(np.linalg.matrix_power(var4,0))   #we get diagonal matrix
print()
print(np.linalg.matrix_power(var4,-2))  #matrix multiplied by -2
print()


 # 5-DEterminate Function...(np.linalg.det())
var5=np.matrix([[1,2,3],[8,4,3],[1,2,3]])
print(var5) 
print()
print(np.linalg.det(var5))   #it return-0,because 2 rows are same
print()

var6=np.matrix([[1,2,3],[8,4,3],[5,2,3]])
print(var6)
print()
print(np.linalg.det(var6))






