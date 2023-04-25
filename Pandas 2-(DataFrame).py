# DataFrame

import pandas as pd
l=[1,2,3,4]
var=pd.DataFrame(l)
print(var)
print(type(var))

dic={'a':[2,4,6],'b':[5,7,3],'c':[3,5,2]}
var2=pd.DataFrame(dic)
print(type(var2))
print(var2)
print()
print(var2["a"][2])           # slicing..getting second value of column 'a

print(pd.DataFrame(dic,index=['e','f','g']))            # put index name
print(pd.DataFrame(dic,columns=['b']))                  # getting specific column

list_1=([3,5,6,7],[5,4,3,7])
var3=pd.DataFrame(list_1)             
print(var3)
print(type(var3))

sr={'a':pd.Series([2,3,4,5]),'b':pd.Series([4,5,6,7])}
sr1=pd.DataFrame(sr)
print(sr1)
print(type(sr1))

# Arithematic Operation

var=pd.DataFrame({'a':[1,2,3,4],'b':[4,5,6,8]})
print(var)
print()

var['C']=var['a'] + var['b']            # Addition
print(var)

var['D']=var['b'] - var['a']              # Subtraction
print(var)

var['E']=var['b'] * var['a']              # Multiplication
print(var)

var['F']=var['b'] / var['a']              # Division
print(var)
print()

var['python']=var['a'] >=3                # LOGICAL OPERATOR
var['java']=var['b'] <=5
print(var)


# DELETE & INSERT DATA     (insrt,pop/delete)

var=pd.DataFrame({'a':[1,2,3,4],'b':[4,5,6,8]})
print(var)

var.insert(1,'p1',var['a'])         #  inserting data
print(var)
print()
var.insert(2,'p2',[1,6,7,4])
print(var)

var['java']=var['b'][:2]                  # copying data  
print(var)
print()

var2=pd.DataFrame({'a':[1,2,3,4],'b':[4,5,6,8],'c':[4,6,7,8]})
print(var)
print()

var3=var2.pop('b')
print(var3)
print(var2)





