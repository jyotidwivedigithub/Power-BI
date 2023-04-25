#   1-Map Function.................
numbers=['1','3','4','5','8']
#for i in range (len(numbers)):
    #numbers[i]=int(numbers[i])
numbers=list(map(int, numbers))  #map function use in place of defined function for converting list value string to integer.
print(numbers)


def squ(a):
    return(a*a)

num=[2,3,4,5,6,7,8,9]
square=list(map(squ, num))
#square=list(map(lambda x:x*x, num))       #use map function with lambda function
print(square)

# run to function together
def square(a):   
    return(a*a)
def cube(a):
    return(a*a*a)

func=[square, cube ]

for i in range(6):
    val=list(map(lambda x:x(i), func))
    print(val)



#   2-FIlter Function.......
list_1=[1,3,5,6,7,9]

def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5, list_1))          #it will return value greater than 5
print(gr_than_5)
  

#   3-Reduce Function.......functools
from functools import reduce
list_2=[2,4,6,8]
num=reduce(lambda x,y:x+y, list_2)
print(num)
num1=reduce(lambda x,y:x*y, list_2)
print(num1)


        





