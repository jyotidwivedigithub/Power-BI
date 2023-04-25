# DATA Analysis-is a process of inspecting,cleansing,transforming and modelling data with the goal of disco-
#    -vering useful information,informing conclusions, and supporting decision-making.
# The name "Pandas" has reference to both "Panel Data",and "Python data analysis" and was created by was ---
#       Mckinney in 2008.
# Pandas is a python library used for working with data set.
# It has functions for anlyzing,cleansing,exploring and manipulating data.
# It has Read and write data structure and different format: csv,text XML,JSON,ZIP etc.
# TYPES of Pandas Data Structures.....
#      1-Series:- 1-Dimensional labeled arrays pd.Series(data).
#      2-DataFrames:- 2-Dimensional data structure with columns,much like a table.
#      3-Panel:- A panel is a 3-Dimensional container on data.
# IMPORT- import pandas as pd
#Importance:-1.Pandas allows us to analyze big data & make conclusion based on statistical theories.
#      2.Pandas can clean messy data sets,and make them readable and relevant.
#      3.Easy handling of missing data(represented as NaN)in floating and non-floating point data.
#      4.Size mutability columns can be inserted and deleted from DataFrame and higher dimensional object.
#      5.Data set merging and joining.Flexible reshaping and pivoting of data set Process time series functionally.
#      6.The pandas provides two data structures for processing the data.

### Series & DataFrame and Panel...

# Series:-It is defined as a 1-D array that is capable of storing various data types...a=pd.Series()
import pandas as pd
x=[2,3,4,5,6]
var=pd.Series(x)
print(var)
print(type(x))

var=pd.Series(x,index=["a","b","c","d","e"])       # for indexing
print(var)

var=pd.Series(x,index=["a","b","c","d","e"],dtype="float",name="python")    #float-change datatyppe  
print(var)
print(var['b'])                                    # sciling

dic={'name':['python','c++','java'], 'no.':[94,75,83],'rank':[1,3,2]}
var1=pd.Series(dic)
print(var1)
print(type(var1))

s=pd.Series(12)
print(s)
s1=pd.Series(12,index=[1,2,3,4,5])               # ceating series
print(s1)


s1=pd.Series(12,index=[1,2,3,4,5]) 
s2=pd.Series(12,index=[1,2,3]) 
print(s1+s2)


