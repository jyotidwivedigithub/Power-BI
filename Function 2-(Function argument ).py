def average(a, b):     
    print("The average is ", (a+b)/2)
average(5,7)

def average(a=5, b=6):
    print("The average is ", (a+b)/2)
average()

            #Types of Arguments
# 1.-DEFAULT ARGUMENT--where we can provide default value while creating a function..function assumes a default value if a value is not provided in function
def average(a=4, b=7):
    print("The average is ", (a+b)/2)
average(4, 3)             #here it will take 4,3 and ignore above given value(4, 7)

def average(a=7, b=4):
    print("the average is ", (a+b)/2)
average(a=6)             #here a=6, b=4    and ignore above given value a=7

def subtraction(a=7,b=4):
    print("the subtraction of a,b", a-b)
subtraction()

def name(fname , mname = "Kumar" , lname ="Dwivedi"):
    print("Hello,", fname, mname, lname)
name("Nitin") 

#2.-KEYWORD ARGUMENT--order in which the argument are passed not in order but get output in order
def name(fname, mname, lname ):
    print("Hello,", fname, mname, lname)
name(mname = "Kumar", fname = "Deepak", lname = "Dwivedi")


#3.-REQUIRED ARGUMENT--
#ex1.-when number of arguments passed doeS not match to the actual function definition
#def name(fname, mname, lname)
#  print("Hello,", fname, mname, lname)
#name("peter", "blau")           #here will be TypeError:name() missing 1 required positional argument: 'lnama'

#ex2.-when number of argument passed matches to the actual function definition
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("naman", "kumar", "sharma")


#4.-ARBITRARY ARGUMENT--For creating a function pass a * before parameter name..The fuction accesses the arguments by procrssing them in the form of tuple.
def name(*name):                                           # (*-args)
    print("Hello,", name[0], name[2], name[2])
name("om", "kumar", "dwivedi")

def average(*numbers):
 print(type(numbers))       #<class 'tuple'>
 sum=0
 for i in numbers:
    sum = sum+i
 print("Average of is:", sum/ len(numbers))
average(9, 7)


#5.-KEYWORD ARBITRARY ARGUMENT--for creating a function pass a ** before parameter name the function accesses the argument by processing them in form of dictionary.
def name(**name):                                        # (**-kwargs)
    print(type(name))         #<class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(fname= "Raj", lname= "Dwived", mname= "Kumar")



   # RETURN STATEMENT...Is used to return the value of expression back to the calling function
def averge(*numbers):
  sum=0 
  for i in numbers:
    sum = sum + i
  # print("Average is:", sum / len(numbers))
  return 3               #return means go back with the given value...3
  return sum / len(numbers)
c = average(7, 8, 3, 9)
print(c)


  
