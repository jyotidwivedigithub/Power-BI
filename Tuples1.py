#tuple can't be change....tuple store multiple item in single variable tuple item separated by commas and enclosed()

tup = (1, 2)
print(type(tup), tup)

tup = (2, )
print(type(tup), tup)
#tup[0]=90    can't use tuple in the form of list[]

tup = (2, 3, 4, "red", "green")
print(type(tup), tup)

#1. POSITIVE TUPLE INDEXING
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[4])

#2. NEGATIVE TUPLE INDEXING
print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])
print(tup[-5])

#3. Check for item      ...we can check if given item present in the tuple this is done using {in} keyword
country = ('Spain', 'India', 'Nepal', 'China')
if 'Nepal' in country:
    print("Nepal is present")
else:
    print('nepal is absent')

#4. Range of Index     ...range can be print by specifying where we want to start and end if we want to skip element in between the range.
#SYNTAX:Tuple[start :end : jumpIndex]

#Ex. printing element within a particular range:
animal = ("cat", "dog", "bear", "deer", "horse")
print(animal[1:3])
print(animal[-4:-1])

#Ex. printing all eliments from start to a given index
print(animal[:4])
print(animal[:-4])

#Ex. print alternate value
print(animal[::2])
print(animal[1:4:2])
