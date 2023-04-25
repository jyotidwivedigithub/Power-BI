#Dictionary is an...
# unorder data type..
# key / value..
# {  }


#Create Dictionary

d={             #d(dictionary) is Key   and   { } is value
 'name':'python',
 'fees':'2000',
 'duration':'2 year'
 }
#Access elements from a dictionary
n=d['name']
print(n)
n=d['fees']
print(n)
n=d['duration']
print(n)

#Iterating through Dictionary
for n in d:
    print(d[n])