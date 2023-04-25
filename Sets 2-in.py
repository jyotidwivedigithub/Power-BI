#JOINING SETS Through many functions.we can perform operations like union and intersection on the sets just like in mathematics

# 1-UNION() and UPDATE()
S1={'red','black','green','orange'}
S2={'gray','black','violet','red'}
S3=S1.union(S2)                                
print(S3)

S1.update(S2)
print(S1)


# 2-INTERSECTION() and UPDATE()
l={12,43,54,32}
b={12,54,42,65}

S=l.intersection(b)
print(S)

l.update(b)
print(l)


# 3-SYMMETRIC_DIFFERENCE() and SYMMETRIC_DIFFERENCE_UPDATE()
M1={10,20,30,40}
M2={11,20, 22,33,44}
M3=M1.symmetric_difference(M2)
print(M3)

M1.symmetric_difference_update(M2)
print(M1)


# 4-DIFFERENCE() and DIFFERENCE_UPDATE()
K1={11,22,33,44,55}
K2={22,24,55}
K3=K1.difference(K2)
print(K3)

K1.difference_update(K2)
print(K1)


