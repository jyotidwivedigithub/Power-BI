# 1-A..
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and row!=0)or((row==0 or row==3)and(col>0 and col<4)):      #pattern-1
        #if (col==0 or col==4)or((row==0 or row==3)and(col>0 and col<4)):                 #pattern-2
            print("*",end="")
        else:
            print(end=" ")
    print()

# 2-B..
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):  #pattern-1
        #if (col==0 or col==4) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):                                      #pattern-2
            print("*",end="")
        else:
            print(end=" ")
    print()

# 3-C..
for row in range(7):
    for col in range(5):
        if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0)):       #pattern-1
        #if (col==0) or ((row==0 or row==6) and (col>0)):                              #pattern-2
            print('*',end=' ')
        else:
            print(end=" ")
    print()

# 4-D..
for row in range(7):
    for col in range(5):
        if (col==0)or (col==4 and (row!=0 and row!=6)) or((row==0 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# 5-E..
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3 or row==6) and (col>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# 6-F..
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and (col>0)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()


# 7-G..
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=1 and row!=2)) or((row==0 or row==6)and (col>0 and col<4)) or (row==3 and (col==3 or col==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# 8-H..
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or(row==3 and (col>0 or col>4)):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 9-I..
for row in range(7):
    for col in range(5):
        if (col==2) or  ((row==0 or row==6) and col!=2):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 10-J..
for row in range(7):
    for col in range(5):
        if (col==2) or (row==0 and col!=2) or (row==6 and col<2):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 11-K..
i=0
j=4
for row in range(7):
    for col in range(5):
        if (col==0) or (row==col+2 and col>1):
             print("*",end="")
        elif((row==i and col==j) and col>0):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()

# 12-L..
for row in range(7):
    for col in range(5):
        if (col==0) or (row==6 and col>0):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 13-M..
for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or (row==col and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 14-N..
for row in range(6):
    for col in range(6):
        if (col==0 or col==5) or (row==col and (col>0 and col<5)):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 15-O..
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 16-P..
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and (col>0 and col<4)) or (col==4 and (row==1 or row==2)):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 17-Q..
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 or row==6)and (col>0 and col<4)) or (row==5 and col==1) or (row==7 and col==3):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 18-R..
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and(row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)) :
             print("*",end="")
        else:
            print(end=" ")
    print()

# 19-S..
for row in range(7):
    for col in range(5):
        if (col==0 and (row>0 and row<3)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)) or ((col==4 and (row>3 and row<6))):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 20-T..
for row in range(5):
    for col in range(5):
        if col==2 or (row==0 and col!=2):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 21-U..
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or (row==6 and(col>0 and col<4)):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 22-V..
for row in range(4):
    for col in range(7):
        if (row==col) or (row==3 and col==3) or (row==2 and col==4) or (row==1 and col==5)or (row==0 and col==6):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 23-W..
for row in range(4):
    for col in range(7):
        if (col==0 or col==6) or (row==1 and col==4) or (row==2 and col==5) or (row==0 and col==3) or (row==1 and col==2) or (row==2 and col==1):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 24-X..
for row in range(5):
    for col in range(5):
        if (row==col) or (row==0 and col==4) or (row==1 and col==3) or (row==3 and col==1) or (row==4 and col==0):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 25-Y..
for row in range(5):
    for col in range(5):
        if (col==2 and (row>1)) or (row==col and col<2) or (row==1 and col==3)or (row==0 and col==4):
             print("*",end="")
        else:
            print(end=" ")
    print()

# 26-Z..
for row in range(6):
    for col in range(6):
        if (row==0 or row==5) or (row==1 and col==4) or (row==2 and col==3) or (row==3 and col==2) or (row==4 and col==1):
             print("*",end="")
        else:
            print(end=" ")
    print()

