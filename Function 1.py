#types of FUNCTION----1.(built in function)  2.(user defined function)

#user-defined functions---we can create function to perform task as per our needis called...
#syntax:
def function_name(parameters):      #def islesser(a, b):
    pass                                #pass              (break continue,pass function)
#Code and Statements

def calculateGmean(a, b):    #for calculating Gmean(geometric mean)
    mean = (a*b)/(a+b)
    print(mean)

                    #we can also use if-else with calculateGmean

def isGreater(a, b):              #for finding greater no.
   if(a>b):
    print("First no. is greater")
   else:
    print("Second no. is greater")

def islesser(a, b)  :             #for finding greater no.
   if(a<b):
    print("First no. is lesser")
   else:
    print("Second no. is lesser") 


a=9
b=7
#if(a>b):                              
 #   print("First no. is greater")
#else:
 #   print("Second no. is greater") 
isGreater(a, b)                       #we can use isGreater/islesser instead of given above
#gmean = (a*b)/(a+b)
#print(gmean)
calculateGmean(a, b)                  #we can use calculateGmean instead of given above

c=5
d=6
islesser(c, d)                         
calculateGmean(c, d)                  



#calling a function
def name(fname, lname ):
    print("Hello,", "Robin", "Hud")
name("Robin,", "Hud")    

