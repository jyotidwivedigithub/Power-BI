# F-String...The format() method formats the specified value(s) and insert them the string's placeholder.
# the placeholder...is defined using curly brackets:{}.

#named indexes: 
txt1="Welcome to {fname} {lname}".format(fname = "Wscube",lname="Tech")

#numbered indexes: 
txt2="Welcome to {0} {1}".format( "Wscube","Tech")

#empty placeholders: 
txt3="Welcome to {} {}".format( "Wscube","Tech")

print(txt1)
print(txt2)
print(txt3)


w="welcome {} to {} WscubeTech" .format("hello", 20);
print(w)

    #  OR

w="Welcome {0} to {1} WscubeTech" .format("hello",20);
print(w)

w="Welcome {1} to {0} WscubeTech" .format("hello",20);
print(w)

w="welcome {a} to {b} WscubeTech" .format(a=20,b=30);
print(w)

w='welcome {a:8} to {b:6} Wscube' .format(a=6,b=10);   #a:8..means it tech 8 space (-------8) and b:10 (--------10)
print(w)                                               #a:8, b:6....it gives lengh f character

w="welcom {a:^8} to {b:<6} Wscube" .format(a=6,b=1)    #^ means 8 a comes between (--------) and < means b comes in left
print(w)

