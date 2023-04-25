# CSV (Comma Separated Values)
# Difference between CSV & XLS(excel) file formate.
#  1.CSV file is a plain text format in which values are separated by commas(comma separated values)
#  2.XLS file format is an Excel Sheets binary file format which holds information about all the worksheets in a file,including both     and formatting


# Write CSV File.....

import pandas as pd
dic={'a':[2,4,6],'b':[5,7,3],'c':[3,5,2]}
d=pd.DataFrame(dic)
print(d)
print()

d.to_csv("New.csv")                      # create new file
d.to_csv("New1.csv",index=False)         # to delete index
d.to_csv("New2.csv",header=[1,2,3])      # to header(a,b,c) name


# Read CSV File...A simple way to store big data sets is to use CSV files.
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

import pandas as pd
csv_1=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv")
print(csv_1)

csv_2=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",nrows=1)    #to get single row
print(csv_2)
print(type(csv_2))
print()

csv_3=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",usecols=["Gender"])   #to get single column
print(csv_3)
#print()

#csv_3=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",skiprows=1)       #to skip rows
#print(csv_3)

#csv_4=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",index_col="Gender")   #change index   
#print(csv_4)
#print()

#csv_5=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",header=3)   #change header..3 row become header
#print(csv_5)
#print()

csv_6=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",header=None)   # to delete header name 
print(csv_6)  

csv_7=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",header=None,prefix="col")   # to set header name after deleting
print(csv_7) 

csv_8=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv",dtype={"EmployeeNumber":"float"})
print(csv_8)                                                   











