#JSON..(Java Scipt Object Notion)..mainly used for storing and transforming data between the browser and the server
#JSON is text,written with JavaScript object notion
#Python too support JSON with a built-in-package called json
#JSON support...(string,number,boolean,null,object,array)
#in Python json exists as a string..Exampe--p='{"name":"Ws","lang":["Pytho","Java"]}'


#    DUMP() function

import json
l={'name': 'zyan','age':'20 year'}
m=json.dumps(l)                    #json.dumps()-for store data
print(m)

import json
d={
    'course':'Python',
    'duration':'3 month'
}
f=json.dumps(d)
print(type(f))
print(f)

#     LOAD()  function ...is used to convert JSON to Python object(python dictionaty)

import json
d='{"name":"kamal", "age":"20 year"}'      #json.load()..for converting json format file to python dictionary
l=json.loads(d)
print(type(l))
print(l)

for a in l:                                 #for iterating data
    print(a)                                #iterating key
    print(a,l[a])                           #iterating vboth key and value

