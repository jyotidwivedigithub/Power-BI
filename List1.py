l=[2, 3, 4, 5, 9]      #order collection of data items
print(l)
print(type(l))

marks = [4, 6, "hari", True]
print(marks)
print(type(marks))
print(marks[0])      #positive index
print(marks[1])
print(marks[2])
print(marks[3])
#print(marks[4])      #error because there are only 4 value (0,1,2,3) in marks given not fifth

#print(marks[-3])      #Negative index
#print(marks[len(marks)-3]) #positive index
#print(marks[4-3])     #positive index
#print(marks[2])       #positive index


## Check whether an item is present in the list or not?
number = [4, 6, "Ram", 3, 8]
if 7 in number:
    print("Yes")
else:
    print("No")   

if "Ram" in number:
    print("Yes")
else:
    print("No")

if "am" in "Ram":         #same things applies for strings as well!
    print("Yes")
else:
    print("No")


#RANGE OF INDEX
marks = [3, 4, 2, 1, 8]
print(marks)
print(marks[:])
print(marks[0:len(marks)])
print(marks[1:])
print(marks[2:4])
print(marks[1:2:3])
print(marks[1:-2])

#Ex.-Printing alternative
animal = ["cat", "dog", "wolf", "bear", "camel"]
print(animal)
print(animal[::3])     #it will give first and third value(0,3)=(cat,bear)
print(animal[1:4:2])

#Ex.-printing every 3rd cosecutive value within a given range
p = ["red", "green", "yellow", "blue", "orange"]
print(p[0:4:3])
print(p[1:4:3])


#LIST COMPREHENSION---are used for creating new lists from other iterables like lists,tuples,dictionaries sets,and even in arrays and string
   #SYNTEX:List=[Expression(item)for item in iterable if condition]

lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]   #return square of 2.4.6.8
print(lst)

l=[]
for a in range(1,50):
    l.append(a)
print(l)

n= [h for h in range(1,50) if h%2==0 ]
print(n)

s="hello"         #convert string into list
d=[g for g in s]
print(d)