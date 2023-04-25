#Inheritance..if we have two class a,b...if we have to inherit(take) all properties of class a in class b then we should use Inheritance
# In Inheritance we can call both class a and b methods by single object
#TYPES-
   #1.-Single Inheritance..where we  call class a properties in class b
   #2.-Multiple Inheritance..where we  call class a properties in class b and class b properties in class c
   #3.-Multilevel Inheritance..where we call class a ans b properties in class c

class A:
    def displayA(self):
        print("Welcome to India A")

class B(A):                             #Single Inheritance
#class B:
    def displayB(self):
        print("Welcome to India B")

class C(B):                               #Multi Inheritance
#class C(A,B):                          #Multiple Inheritance
    def displayC(self):
        print("Welcome to India C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()



