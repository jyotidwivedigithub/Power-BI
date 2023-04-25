#user-defined modules
def sum(a,b):
    c=a+b
    return(c)

def mul(a,b):
    c=a*b
    return(c)

import Modules1
print('modules1',sum(12,23))

import Modules1 as m
print(m.sum(12,43))
print(m.sum(11,23))

from Modules1 import sum
print(sum(34,43))

from Modules1 import *
print(mul(12,11))