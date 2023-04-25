# Anonymous/Lambda Function..it is a new way to make function.. nothing else
def add(a, b):
    return(a+b)

minus = lambda x, y:x-y
#def minus(x, y):
   # return(x-y)
print(minus(9, 6))


#....OR...

def a_first(a):
    return a[1]

a=[[4,5],[12,8],[11,4]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)