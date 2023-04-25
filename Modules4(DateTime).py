#Built-in modules
#("%b")-  Month name,short version - Dec
#("%B")-  Month name,full version- December
#("%m")-  Month as a number 1-12-2022 - 12
#("%y")-  Year,short version,without century(2022) -22
#("%Y")-  Year,full version -2018
#("%H")-  Hour 17:23 -  17 hr    
#("%I")-  Hour 17:30 -  5 hr
#("%p")-  AM/PM
#("%M")-  Minute 12-50 -  50

#SYNTAX:=now.strftime("%Y")
#print("year:",year)
import datetime

x=datetime.datetime.now()               #return current date
print(x)

m=x.strftime("%y")      #("%y")-  Year,short version,without century(2022) -22
print(m)

m=x.strftime("%Y")      #("%Y")-  Year,full version -2018
print(m)

m=x.strftime("%b")      #("%b")-  Month name,short version - Dec
print(m)

m=x.strftime("%B")      #("%B")-  Month name,full version- December
print(m)

m=x.strftime("%m")      #("%m")-  Month as a number 1-12-2022 - 1
print(m)

m=x.strftime("%H")      #("%H")-  Hour 17:23 -  17 hr  
print(m)

m=x.strftime("%I")      #("%I")-  Hour 17:30 -  5 hr
print(m)

m=x.strftime("%p")      #("%p")-  AM/PM
print(m)

m=x.strftime("%M")      #("%M")-  Minute 12-50 -  50
print(m)

print(datetime.datetime(2022,11,21))    #yr-mm-dd..find date

