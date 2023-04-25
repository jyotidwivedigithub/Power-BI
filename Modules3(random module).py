#  RANDOM MODULES....it is in-built function

#1.-RANDOM.RANDIT() method
import random
n=random.randint(2,8)     #return a no between 2 and 8 (both included)
print(n)

#2.-RANDOM.RANGE() method
n1=random.randrange(3,9)      #return a no.between 3(included) and 9(not included)
print(n1)

#3.-RANDOM.CHOICE() method
l=[1,3,5,6,4,9]
c=random.choice(l)        #return a random element from a list
print(c)
#print(random.choice(l))

#4.-RANDOM.RANDOM() 
r=random.random()         #returns a random float number between o and 1
print(r)

#5.-RANDOM.SHUFFLE()
l=[12,34,35,41]           #take a sequence and returns the sequence in a random order
random.shuffle(l)
print(l)

#6.-RANDOM.UNIFORM()
u=random.uniform(3,9)     #returns a random float number between two given parameters
print(u)

