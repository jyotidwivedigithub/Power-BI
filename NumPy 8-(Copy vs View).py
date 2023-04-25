   #both are used for copy 
# copy function   
import numpy as np            
var=np.array([1,2,3,4])           
co=var.copy()
var[1]=40                 # basic difference b/w copy and view
print("var : ",var)
print("copy : ",co)

print()


# view function 
x=np.array([2,4,6,8])                
vi=x.view()
x[1]=40                   # basic difference b/w copy and view
print("x : ",x)
print("view : ",vi)


