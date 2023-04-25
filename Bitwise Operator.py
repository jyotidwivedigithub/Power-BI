# & - AND- x & y
# | - OR - x | y
# ^ - XOR - x ^ y

#  A     B      A & B      A | B         A ^ B
#  0     0        0          0             0
#  0     1        0          1             1
#  1     0        0          1             1
#  1     1        1          1             0

# 1= TRUE      0= FALSE

x=10
y=8

print(bin(x))
print(bin(y))

print(x&y, bin(x&y))          # & condition
print(x|y, bin(x|y))          # | condition
print(x^y, bin(x^y))          # ^ condition



x=5
y=5

print(bin(x))
print(bin(y))

print(x&y, bin(x&y))          # & condition
print(x|y, bin(x|y))          # | condition
print(x^y, bin(x^y))          # ^ condition
