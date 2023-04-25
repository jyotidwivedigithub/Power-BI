# 1-Is:-returns True if both variables are the same object...Example- x is y.
# 2-Is Not:- return True if both variables are not the same object...Example- x is not y.

x=10
y=10

print(x is y)              # is operator
print(x==y)

print(x is not y)          # is not operator
print(x!=y)


x=23
y=45

print(x is y,x==y)
print(x is not y,x!=y)