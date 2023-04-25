# Pattern-1
num=int(input("Enter the no. of rows:"))
for i in range(0,num):
  for j in range(0,num-i-1):
    print(end=" ")
  for j in range(0,i+1):
    print("*",end=" ")
  print()



# Pattern-2
num=int(input("Enter the no. of rows:"))
for i in range(0,num):
  for j in range(0,num-i-1):
    print(end=" ")
  for j in range(0,2*i+1):
    print("*",end="")
  print()


#Printing REVERSE Pyramid
num=int(input("Enter the no. of rows:"))
for i in range(num,0,-1):
  for j in range(0,num-i):
    print(end=" ")
  for j in range(0,i):
    print("*",end=" ")
  print()