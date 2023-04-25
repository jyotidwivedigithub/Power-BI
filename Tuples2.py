   # MANUPULATING TUPLES...Tuples are immutable, hence if ou want to add,remove or change tuple items, then first you must convert the tuple to alist then perform operation on that list and covert it back to tuple
countries = ("Spain", "Japan", "Nepal", "China")
tem = list(countries)
tem.append("India")        #add item
tem.pop(3)                 #remove list
tem[2] ="USA"              #change item
countries = tuple(tem)
print(countries)

  #.....TUPLE METHOD/FUNCTION.......

tuple = (1, 2, 4, 5, 8, 3, 3, 4, 4, 9)
res = tuple.count(4)              #count the no of times of item
print('cont of 4 in Tuple is:', res)


#SYNTAX:tuple.index(element, start,end)
res = tuple.index(3)              #return the first occurence of the given element from tuple
print('first first occurrence is', res)


#for min() and max()
t=(12,12,34,32,43)
m=min(t)        #for min()
print(m)

n=max(t)        #for max()
print(n)

c=sum(t)        #for sum
print(c)


#EX.2-Good Morning Sir
#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. your program should use
#--use time module to get the current hour. Here is a sample program and documentation link for you
import time
t = time.strftime('%H:%M:%S')    #for finding time
print(t)
t = time.strftime('%H')          #for hour
print(t)
t = time.strftime('%M')          #for minute
print(t)
t = time.strftime('%S')          #for second
print(t)


t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))    #to check greeting according to time
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif (hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")




