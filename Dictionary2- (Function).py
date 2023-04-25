# get( )
# keys( )
# value( )
# items( )
# del
# pop( )
# dict( )
# update( )
# clear( )
d={
    'name':'komal',
    'height':6.7,
    'age':'23 year',
}

c=d.get('name')       #d.get( )...return both keys or  values 
#c1=d['name']
print(c)

for n in d.keys():    #d.keya( )...return keys
    print(n)

for n in d.values():  #d.values( )...return values
    print(n)

for a,b in d.items():   #d.items( )...return both keys and values
    print(a,b)
  
  #Delete Function

del d['age']         #del d[ ]..delete the both keys or values 
print(d)

d.pop('name')         #d.po.[ ]...delete function
#print(d.pop('name'))
print(d)

d=dict(name='komal', height=6.7) #for creating dictionary
print(d)

    
d={                   #Updating Dictinary
    'student':'kavita',
    'fees':'30000',
    'duration':'3 year'
}

d.update({'student':'sunny'})
print(d)

d.clear()           #delete all data of dictionary ...return[ ]
print(d)



