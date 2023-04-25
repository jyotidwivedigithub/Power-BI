## pattern-1...
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end="")
    print()



## pattern-2...   
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(j+1,end="")
    print()



## pattern-3...
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i+1):             #col of no. doesn't matter here because we print no here
        print(i+1,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end="")
    print()



##pattern-4...
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i,-1,-1):             #col of no. doesn't matter here because we print no here
        print(n-i,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(n-1,end="")
    print()



##pattern-5...
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i+1):
        print(n-j,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(n-j,end="")
    print()



##pattern-6...
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j,end="")
    print()

#Reverse
n=int(input("Enter the no. of rows needed:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(n-j,end="")
    print()
