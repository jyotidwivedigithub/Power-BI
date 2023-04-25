#STRING METHOD
#(String are immutable)
a="kanchan"     #a is string
print(len(a))               #length of string
print(a.upper())            #uppercase=print(str.upper())....capitalise all letter
print(a.lower())            #lowercase=print(str.lower())....convert all letter in small letter

b=" Komal sharma "
print(b.strip())            #strip=print(str.strip())...remove any white spce before and after string

c="kamal !!!!!!"
print(c.rstrip("!"))        #rstrip=print(str.rstrip())...removes any trailing ("!") characters

d="kajal"
print(d.replace("a", "o"))  #replace=print(str.replace("a", "o"))...replace all accurances of a stringwith another string

e="God Rama"
print(e.split(" "))        #split=print(str.split(""))...it specified the instance and retuns the separated string as list iten

introduction= "krishna is a adorable god."
print(introduction.capitalize())   #capitalize=print(str.capitalize())...it convert first letter in uppercase rest in lowercase

str= "Welcome to the World.!!!"
print(len(str))                    #len function
print(len (str.center(48)))        #centre with len=print(len(str.center(2*given character)))...align the string to the center as per the parameter given by user.
#print(str.center(13))             no changes because parameter given by user (13) is wrong it would be (48)
print(str.center(48, " "))         #center=(str.center(2*no of given character, " ")...OUTPUT= (............Welcome to the World.!!!............)

str1= "!!!Rani!! !!!!!!!!! Rani"    #first letter should be capital
print(str1.count("Rani"))          #it give the no. of repeatition of given occurance

str2="gita is very intelligent girl.!!!"
print(str2.endswith("!!!"))         #endswith=print(str.endswith(" "))...output=true..check the given value is 'True,or,False

#we can also check for a value in between the string by by providing start and end index position.
print(str2.endswith("s", 3, 7))     #True

str3="Sita's kitchen is very very clean"
print(str3.find("is"))        #print(str.find(" "))...it gives index of first given occurance...14
print(str3.find("s"))         #output-5

#print(str3.find("oops"))     #output-(-1)...because if given value is absent from the string then return -1.

print(str3.index("is"))
#print(str3.index("oops"))    #if given value is absent from string then raise an exception/error
print(str3.index("kitchen"))  #if given value is present from string then return the first index whereit is present.

str4="WelcomeToTheWorld"
print(str4.isalnum())       #isulnum=print(str.isulnum())...it returns True only if the entire string only consist of A-Z,a-z,0-9
                            
str="welcome@123"    #if any other character are present then it return false
print(str.isalnum())   #return false because it has...@.its a symbol

str="welcome"
print(str.isalpha())       #ishalpha=print(str.isalpha())...it return True only if string is only consist of A-Z,a-z
#if any other characters or number(0-9) are present then it return False.

str=("Welcome To World")   
print(str)
l=str.split();             #=str.split();---convert String to List in python using SPLIT FUNCTION
print(l)

str=("134")  
print(str.isdigit())       #=str.isdigit( )...it gives true if given string consist of digits not alphabet  else false
