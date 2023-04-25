   # BREAK STATEMENT---enable a program to skip over apart of the code. it terminate the very loop it lies within.
for i in range(11):
    print("5 * ", i+1, "=", 5*(i+1))
    if (i==10):
      break
print("skip the loop")

for b in range(1,101,1):
    print(b, end=" ") 
    if(b==50):
        break
    else:
        print("missing")


  # CONTINUE STATEMENT---Skip the rest of the loop statement and causes the next iteration to occure
for k in range(12):
    if(k==10):
     print("Skip the iteration")
     continue
    print("5 x", k+1, "=", 5*(k+1))

for j in [2,3,4,5,6,7,8,0]:
    if(j%2!=0):
     continue
    print(j)