#1-input, 2-for loop,  3-range(),  4-print()

#...Printing stars "*" in Right Angle Traingle Shape...

 # Pattern-1
num=int(input("Enter the no. of rows:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
        #print("a",end=" ")
        #print("1",end=" ")
    print()

 # Pattern-2
num=int(input("Enter the no. of rows:"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end=" ")
        #print("1",end=" ")
    k=k+2
    print()


#...Printing REVERSE stars "*" pattern...
num=int(input("Enter the no. of rows:"))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
        #print("a",end=" ")
        #print("1",end=" ")
    print()




    




        
