#NESTED DICTIONARY(Putting dictionary inside another dictionary)..it is a collection of dictionaries into one single dictionary.
#Create a Nested Dictionary...

course={
    'phd':{'duration':'3 month', 'fees':10000},
    'c++':{'duration':'4 month', 'fees':12000},
    'python':{'duration':'5 month', 'fees':1500},
}

print(course)
course['c++']['fees']=20000  #for updating value
print(course['c++']['fees'])

print(course['phd'])
print(course['c++'])
print(course['python'])

   #  OR
for k,v in course.items():
    print(k,v)

print(course['phd']['fees'])

for k,v in course.items():  
    print(k,v[ 'duration'],v[ 'fees'])

