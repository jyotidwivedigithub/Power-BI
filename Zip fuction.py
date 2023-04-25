 #  ZIP FUCTION FOR ITERATING  Over 2+list
#it can be used both in LIST AND TUPLE
l=[12,34,12]
l1=[12,34,67]
for a,b in zip(l,l1):
    print(a,b)

s=[1,4,3,5,2]    #here it will ignore extra element 2
s1=[3,2,4,5]
for a,b in zip(s,s1):
    print(a,b)

           #OR... iterating by logic
t=len(l)
for h in range(t):
    print(l[h],l1[h])







