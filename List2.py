 #LIST METHOD/FUNCTION      LIST(l)
l  = [2, 5, 7, 4, 6, 3, 6]

l.reverse()   #l.reverse() METHOD...reverse the list 
print(l)     

l.sort()      #l.sort()  METHOD...sort the list in ascending order
print(l)

c = [2, 3, 4, 5, 3, 4, ]
print(c.index(3))       #l.index() METHOD...return the index of the first occurence of the list item

print(c.count(3))       #l.count() METHOD...return the count of the number of items with the given value

m=max(c)                #maximum
print(m)

b=min(c)                #minimum
print(b)


# Function for UPDATE/REPLACE ELEMENT i list
d=[12,34,56,23]
m = d.copy()            #l.copy() METHOD..return copy of list...it is use to perform operation without modifying the list
m[0] = 0
print(d)

d[0] = 32      #l[ ]...replace /update list
print(d)

d.insert(1, 34)         #l.insert() METHOD...insert item at the given index
print(d)

colour = ["red", "orange", "green", "black"]
colour.insert(2, "blue")
print(colour)

b = [2,3,4,5,1,9]
e = [3,4,6,7,9]
b.extend(e)          #l.extend() METHOD...add an entire list or any other collection datatype(set,tuple,dictionary) to existing list
print(b)

e.append(9)    #l.append() METHOD..to append(add) items to the end of the existing list
print(e)

l=[]
for a in range(1,50):
    l.append(a)
print(l)

n= [h for h in range(1,50) if h%2==0 ]
print(n)


s = [1,3,5,4,2,6]
t = [3,2,4,8,9]
k = s+t          #Concatenating (add) two list...to join two list
print(k)
print(s + t)



# FUNCTIONOF FOR DELETING ELEMENT IN LIST  (only for list)
l=[20,30,42,45]
print(l)

del l[1]            # del[] FUNCTION[]
print(l)

k=[43, 23, 54, 65]
k.pop(0)          #l.pop() FUNCTION for remove the item from list
#print(k.pop())   #it will return the deleted item
print(k)

d=[23,12,32,43]
d.remove(23)      #l.remove() FUNCTION..HERE we have to put the no not index
print(d)

d.clear()         #l.clear()  FUNCTION..it will clear all list return []
print(d)

