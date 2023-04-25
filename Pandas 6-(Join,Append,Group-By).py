### JOIN & APPEND FUNCTION....

# JOIN FUNCTION...

import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})      
var2=pd.DataFrame({"C":[10,20,30,60],"D":[24,25,23,22]})
print(var1.join(var2))

var3=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]},index=["a","b","c","d"])      
var4=pd.DataFrame({"C":[10,20],"D":[23,22]},index=["a","b"])
print(var3.join(var4))
print(var4.join(var3))                                              # reverse data
print(var3.join(var4,how = "outer"))  

ar1=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})      
ar2=pd.DataFrame({"C":[10,20,30,60],"B":[12,13,14,15]})
print(ar1.join(ar2,how = "outer",lsuffix="_11",rsuffix="_11"))     # rsuffix/lsuffix=l= right/left suffix  


# APPEND FUNCTION...
import pandas as pd
ar3=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})      
ar4=pd.DataFrame({"C":[10,20,30,60],"B":[12,13,14,15]})
print(ar3.append(ar4))
print(ar3.append(ar4,ignore_index=True))

m1=pd.DataFrame({"A":[10,20,30,40],"B":[12,13,14,15]})      
m2=pd.DataFrame({"C":[11,22,33,66],"D":[24,25,23,22]})
print(m1.append(m2))
print(m1.append(m2,ignore_index=True))
print(m1.append(m2,ignore_index=False))


### GROUP-BY...Guide to grouping data in python...it return random data
import pandas as pd
var=pd.DataFrame({"name":['a','b','c','d','a','b','a','b','c'],
     "s1":[1,3,4,5,3,4,2,5,2],
     "s2":[11,12,13,34,54,11,12,13,35]})
print(var)

# get all data in group
var_new=var.groupby("name")          # grouping all data by name
print(var_new)
for x,y in var_new:
    print(x)
    print(y)
    print()
    
# get all data seperately
var_new=var.groupby("name")   

print(var_new.get_group("a"))
print(var_new.get_group("b"))
print(var_new.get_group("c"))
print(var_new.get_group("d"))

# get min,max,mean value
print(var_new.min())
print(var_new.max())
print(var_new.mean())

