#STRING (" ")..is a sequence of charecter
name="ram"
print("Hello, " + name)

friend="rani" 
print("hello, " + friend)

anotherfriend="rekha"
print("Hellow," + name, friend, anotherfriend)

apple='He said," i want to eat an apple".'      #apple="he said, "i want to eat apple"---it will be error because of double string
print(apple)

    #MULTIPLE STRING
apple2='''He said,                       
Hi ram
"I want to eat an apple ".'''
print(apple2)

apple3='''he said, "he wants to go  mumbai".'''  #we use tripple string if we want to put double string between the line
print(apple3)

    #CHARACTER OF STRING
R="radhika"
print(R[0])
print(R[1])
print(R[2])
print(R[3])
print(R[4])
print(R[5])
print(R[6])
#print(R[7])        #throws an error because there are only 6 character in radhika-0123456


     #LENGTH OF STRING
print(len("radhika")) 
print(len("mohan"))  
print(len("radhamohan"))

fruit ="mango"
len1 =len(fruit)
print("mango is a", len1, "letter world.")


     #Convert String to List using SPLIT FUNCTION
n=input("Enter the value: ")   #Welcome To World
print(n)
l=n.split();
print(l)



