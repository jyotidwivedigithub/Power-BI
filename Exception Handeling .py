# Type are error which can be handle.......but syntax error can't be handle

 #1.-Zero Division Error         
 #2.-Num Error                  
 #3.-Type Error              
 #4.-Value Error   
 #5.-Index Error     
 #6.-Key Error
 #7.-Module Not Found Error
 #8.-Import Error


#1.-Zero Division Error         
a=10
print(a/0)                           #print(a)

#2.-Num Error    
a=10            

#3.-Type Error                 
print("10" + 10)                       #print(10+10)

#4.-Value Error
#a=int(input("Enter the value")):
a='Hello'                                    #a=10

#5.-Index Error
l=[10,20,30,40]
print(l[5])              #index(0,1,2,3)=(10,20,30,40)

#6.-Key Error
d={'name':'jupiter','fee':'2000'}
#print(d[fees])            #'fees' will error because we have used 'fee'....print9d['fee']

#7.-Module Not Found Error
  #let we make any module name-cal.py but we import cals.py 
#mport cals.py             #cal.py

#8.-Import Error..if we made any module and import right module but function which is call in module is wrong 
 #cal.py
def sum():
    print(10+20)

  #for cal import sum 1      it will import error because sum1 name function is not fount here

