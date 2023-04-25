# to reshape the the pandas file we use 2-function..
#    1.Pivot Table
#    2.Melt Function

### MELT FUNCTION().... pd.melt()...vertically reshape the table

import pandas as pd
var = pd.DataFrame({"days":[1,2,3,4],"eng":[40,43,42,45],"math":[35,42,41,47]})
print(var)

print(pd.melt(var))                      # vertically reshape the table
print(pd.melt(var,id_vars=["eng"]))      # to get/make specific "eng"  as id
print(pd.melt(var,id_vars=["days"]))     # to get/make specific "days" as id

# Customize the data

print(pd.melt(var,id_vars=["days"],var_name="python"))     # change the name of variable
print(pd.melt(var,id_vars=["days"],var_name="wscube"))


### PIVOT TABLE ...pivot()

var = pd.DataFrame({"days":[1,2,3,4],"st_name":["a","b","a","b"],"eng":[40,43,42,45],"math":[35,42,41,47]})
print(var)

print(var.pivot,index="days",columns="st_names")     #saperate name according to specific column
print(var.pivot,index="days",columns="st_names",values="eng")    #value use to get only single data



# Aggfunc() for performing Arithematic Operation in Pivot Table

import pandas as pd
var2 = pd.DataFrame({"days":[1,1,2,2],"st_name":["a","c","a","c"],"eng":[40,43,42,45],"math":[35,42,41,47]})
print(var2)

#print(var2.pivot_table(index= "st_name",columns="days",aggfunc="mean"))     it doesn't work ?

# Margins give average/mean value
#print(var2.pivot_table(index="st_name",columns="days",aggfunc="sum",margins="True"))    it also does't work


