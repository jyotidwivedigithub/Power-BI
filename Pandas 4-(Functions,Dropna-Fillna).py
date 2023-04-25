import pandas as pd
csv_1=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv")
print(csv_1)

# functions of Pandas....
print(csv_1.index)                        # to get index range
print(csv_1.columns)                      # to get column name
print(csv_1.describe())                   # to get count,mean,std,min,max,25%,50%,75% all value 
print(csv_1.head())                       # to get top 5 value
print(csv_1.head(7))                      # to get top 6 value
print(csv_1.tail())                       # to get last 5 value
print(csv_1.tail(8))                      # to get last 8 value

# Split/Slicing
print(csv_1[:2])                          # return all value of row 0,1
print(csv_1[3:7])                         # return value of row 3-6
print(type(csv_1))

# Convert data to Array,  Numpy
print(csv_1.index.array)                  # data convert into Array 
print(csv_1.to_numpy())                   # data convert into Numpy
print()

import numpy as np                        # another function of convert data into numpy
v=np.asarray(csv_1)
print(v)

# Sort Function..
print(csv_1.sort_index(axis=0,ascending=False))   # sorting of data in ascending /descending(True/False) order 

# to change data of row and column(loc[] function)
csv_1.loc[0,"EmployeeNumber"]="Employee"
print(csv_1)

# to get particular data..(loc[],  iloc[] Function)
print(csv_1.loc[[2,3],["EmployeeNumber","Gender"]])   #return 2,3 row no col EmployeeNumber,Gender
print(csv_1.loc[2:3])                                 # return all data of 2,3 row
print(csv_1.iloc[2,3])                                # iloc-return 3 col of 2 index 

# Drop/Delete Row /Column  (drop() function)
#print(csv_1.drop(0,axis=0))                          # drop row 0
#print(csv_1.drop("Gender",axis=1))                   # drop gender col


###.. Handeling missing value  ( DROPNA & FILLNA Function)..
import pandas as pd
var=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv")
print(var)

## DROPNA (.var.dropna())....drop missing value(NaN) according to axis=0/1 (0=row,1=column)

#print(var.dropna())                                # drop all row of Nan value
#print(var.dropna(axis=0))                         # we can also use axis=0/1 to drop NaN value row & col
#print(var.dropna(how="any"))                      # drop all Nan value rows( if any row has even single NaN value)
#print(var.dropna(how="all"))                      # drop only row which has all value NaN
#print(var.dropna(subset=["EmployeeNumber"]))      # drop any specific Nan value along with column

#var.dropna(inplace=True)                           # drop all NaN value and create New Data-Set
#print(var)

#print(var.dropna(thresh = 1))                     # drop single Nan value of a row..here 1= no of NaN value in a row(1/2/3/...)


## Fillna (var.fillna())...

#print(var.fillna("Python"))                         # fill all NaN value
#print(var.fillna({"Gender":"Third Gender"}))        # fill specific row/column NaN value
#print(var.fillna(method = "ffill"))                 # fill col value through ffill/bfill(forward/backward) value
#print(var.fillna(method="ffill",axis=1))            # fill according to axis

#var.fillna(200,inplace=True)                        # replace all NaN value from 11
#print(var)

print(var.fillna("python",limit=2))                  # fill those row which has max.2 NaN value 