# 1-And:-returns True if both Statements are true...Example- x<5 and x<10.
# 2-OR:-returns True if oneof the statements is true...Example- x<5 or x<4.
# 3-Not:-reverse the result,returns False if the result is true...Example- not(x<5 and x<10).

x=10
y=30

print(x==10 and x<y)               # And condition
print(x==10 and x>y)

print(x==10 or x<y or x==y)        # OR conditon
print(x==y or y<x or x>y)

print(not x!=10)                   # Not condition
print(not x==10)