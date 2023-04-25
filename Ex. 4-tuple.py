 #  EX.-GOOD MORNING SIR
#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. your program should use
#--use time module to get the current hour. Here is a sample program and documentation link for you
import time
t = time.strftime('%H:%M:%S')    #for finding time
print(t)
t = time.strftime('%H')          #for hour
print(t)
t = time.strftime('%M')          #for minute
print(t)
t = time.strftime('%S')          #for second
print(t)


t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))    #to check greeting according to time
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif (hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")