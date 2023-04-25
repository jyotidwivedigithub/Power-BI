# USING FOR LOOP     (iterating over a list)

name = "rajkumar"   #character
for u in name:
   print(u) 
   if(u == "j"):
    print("This is so special!")


colors = ["red", "green", "orange", "yellow"]    #list
for color in colors:
  print(color) 
  for i in color:
   print(i)

for k  in range(6):    #range
   print(k)
for k in range(1,9):
   print(k + 3)
for k in range(1, 100):  
   print(k)
for k in range(5,12,4):
   print (k)  

   #USING WHILE LOOP 
i=0
while(i<3):
   print(i)
   i=i+1
print("Done with loop")

k=5
while(k<9):
   print(k)
   k=k+2

while(i<40):
   i=int(input("Enter the no.: "))
   print(i)                         #no will be printed till the no be more than equal to 40

#while i in range(1, 9):
 #  print(i)             output will be error because range can be used in FOR LOOP

c=5        # (DECREMENT WHILE LOOP)---Here c variable is set to5 which  decrement after each iteration, depending upon the WHILE LOOP condition ,we need to either increment or decrement.
while(c>0):    
   print(c)
   c=c-1
 #we can also use else-condition with WHILE LOOP
else:
   print("I am inside else")  

d=-5
while(d>-8):
   print(d)
   d=d-1



   # {Do-While Loop body};---it execte at least once whether condition is TRUE/FALSE and then the repetition of loop's body depend on the condition(TRUE/FALSE).
   # While(condition);
   #Emulation of Do-While Loop in python
i = 0
while True:
   print(i)
   i= i+1
   if(i%50 == 0):
      break


while True:                            #re-check
 num=int(input("Enter the no: "))
 print(num)
 if(num%10 == 0):
      break






