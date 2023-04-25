### MERGE FUNCTION()... to merge two variable one value of both variable should be same

import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
var2=pd.DataFrame({"A":[1,2,3,4],"C":[4,5,3,2]})

print(pd.merge(var1,var2,on="A"))
print(pd.merge(var2,var1,on="A"))                #  to reverse data
print()

# When both common part("A") value is different....return only same vaue

var1=pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
var2=pd.DataFrame({"A":[1,2,6,5],"C":[4,5,3,2]})

print(pd.merge(var1,var2,on="A"))
print(pd.merge(var2,var1,on="A"))
print()

# Merge data passing Inner/Left/Right/Outer
var3=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})       # var3 = left data
var4=pd.DataFrame({"A":[1,2,3,6],"C":[24,25,23,22]})       # var4 = right data

print(pd.merge(var3,var4,how = "inner"))                 # inner return only common data
print(pd.merge(var3,var4,how = "left"))
print()
print(pd.merge(var3,var4,how = "right"))
print(pd.merge(var4,var4,how = "outer"))
print(pd.merge(var4,var4,how = "outer",indicator=True))
print()

# How to find present values of Data-Set....
var5=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})      
var6=pd.DataFrame({"A":[1,2,3,6],"B":[24,25,23,22]})

print(pd.merge(var5,var6))                       # return empty dataframe if both variable name is same
print(pd.merge(var5,var6,left_index=True,right_index=True))   # show empty dataframe
print(pd.merge(var5,var6,left_index=True,right_index=True,suffixes=("name","id")))    # suffixes..gives col name


### CONCAT FUNCTION...join two series ,and two dataframe

sr1=pd.Series([1,2,3,4])                      # Join Series
sr2=pd.Series([11,12,13,14])
print(sr1)
print(sr2)
print(pd.concat([sr1,sr2]))

d1=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})   # Join DataFrame
d2=pd.DataFrame({"A":[1,2,3,4],"B":[24,25,23,22]})
print(pd.concat([d1,d2]))
print(pd.concat([d1,d2],axis=1))              # Join according to axis=0/1

d3=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})   
d4=pd.DataFrame({"A":[1,2],"C":[24,25]})
print(pd.concat([d3,d4]))
print(pd.concat([d3,d4],axis=0))
print(pd.concat([d3,d4],axis=1,join='inner'))  # does not show missig data row show only non NaN row Value
print()

d5=pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})  
d6=pd.DataFrame({"A":[1,2,3,4],"C":[24,25,23,22]})
print(pd.concat([d5,d6],axis=1,keys=["python","java"]))  # keys..to pass key name

d7=pd.DataFrame({"A":[1,2,3,4]})
d8=pd.DataFrame({"A":[1,2,3,4],"B":[24,25,23,22]})
print(pd.concat([d7,d8]))
print()

m1=pd.DataFrame({"A":[1,2,3,4]})
m2=pd.DataFrame({"B":[1,2,3,4],"C":[24,25,23,22]})
print(pd.concat([m1,m2]))