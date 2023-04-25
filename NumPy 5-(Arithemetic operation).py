#a+b...np.add(a,b)                             #np.max()
#a-b...np.subtract(a,b)                        #np.min
#a*b...np.mulyiply(a,b)                        #np.argmin()..np.argmax()..position of variable
#a/b...np.divide(a,b)                          #np.sqrt(x)
#a%b...np.modulas(a,b)    give remainder       #np.sin()
#a**b...np.power(a,b)                          #np.cos()
#1/a...np.reciprocal(a)                        #np.cumsum()..community sum
                                               
# 1-Dimentional.....
import numpy as np
var=np.array([1,2,3,4])    #add
varadd=var+3
print(varadd)

var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])

varadd=var1 + var2         #add
print(varadd)  


varadd=var1 - var2        #subtraction
print(varadd)  

varadd=var1 * var2        #multiplication
print(varadd)  

varadd=var1 / var2        #division
print(varadd) 

varadd=var1 % var2        #modulas%
print(varadd) 

varadd=var1 % 3       #modulas%
print(varadd) 

varadd=var1 ** var2        #power
print(varadd)

varadd=1/ var2        #reciprocal 1/1, 1/2, 1/3, 1/4
varadd=np.reciprocal(var2)
print(varadd)

# 2-Dimensional.....
var21=np.array([[1,2,3,4],[1,2,3,4]])
var22=np.array([[1,2,3,4],[1,2,3,4]])

varadd2=var21 + var22    #add
print(varadd2)

varadd2=var21 - var22    #subtraction
print(varadd2)

varadd2=var21 * var22    #multiplication
print(varadd2)

varadd2=var21 / var22    #division
print(varadd2)

varadd2=var21 % var22    #modulas
print(varadd2)

varadd2=var21 ** var22    #power
print(varadd2)

# 3-Dimensional
var111=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
var222=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])

varadd2=var111 + var222    #add
print(varadd2)

varadd2=var111 - var222   #subtraction
print(varadd2)

varadd2=var111 * var222    #multiplication
print(varadd2)

varadd2=var21 / var22    #division
print(varadd2)

varadd2=var111 % var222    #modulas
print(varadd2)

#Some other function                 axis=0-coloum,  axis=1-row
import numpy as py
var=np.array([1,3,6,5,7,9])
print("min : ",np.min(var),np.argmin(var))    #variable with index no
print("max : ",np.max(var),np.argmax(var))
print("sqrt : ",np.sqrt(var))                 #sqrt(x)-sqare root

var1=np.array([[2,6,4],[1,3,2]])
print(np.min(var1,axis=1))                    #variable with axia/row/column position
print(np.max(var1,axis=0))

var2=np.array([2,4,6,9])
print(np.sin(var2))                       #sin()
print(np.cos(var2))                       #cos() 
print(np.cumsum(var2))                    #community sum()







