#Set has only value not keys like tuple...set is unorder and un index....define by common() and curly{} bracket.
s={10,23,43,21}
for a in s:               #for iterating through a set
    print(a)

#...SET FUNCTIONS/Methods---
#len(s)  set()   add()  pop()  remove()  clear()  discard() update()  isdisjoint()  issuperset()

l=(10,20,43,23)
print(len(l))   #return the length of set

s=set(l)       #for converting into set
print(s)

s={34,64,12,35}
s.add(11)      # for adding extra element/value in set
print(s)

s.pop()        #for deleting any random element from set....here we cannot pass index for deleting any specific element because set is UNINDEX
print(s)

s.remove(34)   # for removing/deleting any specific value through value
print(s)

s.discard(12)  # for deleting any specific value through value
print(s)

s.clear()     #for deleting all data..return set()
print(s)

s={22,24,43,53}
l=[12,23,34]
s.update(l)   #for updating set{}
print(s)

M1={10,23,43,40}    #isdisjoint-is used to check if all items are given  set is present in another set
M2={10,32,54,67}    #if present return true..else false
M3=M1.isdisjoint(M2)
print(M3)

M1={10,23,43,40}    #issuperset-is used to check if all items of particular set is present in original set
M2={10,23,43}    #if present return true..else false
M3=M1.issuperset(M2)
print(M3)


#Check if item is present/absent in set
set={'kerala', 'delhi',12,34,False}
if'kerala' in set:
    print('kerala is present')
else:
    print('kerala is absent')
    



