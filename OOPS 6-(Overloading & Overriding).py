#OVERLOADING - Method overloading is one concept of polymorphism..it comes under OOPS..
# It is worked in same method names and different arguments..Argument different will be base on a number of arguments and types of arguments.

class Area: 
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Ractangle:",(a*b))
        elif a!=None:
            print("Area of Square:",(a*a))
        else:
            print("Nothin to find")

obj=Area()
obj.find_area(10,20)
obj.find_area(10)
obj.find_area()


# OVERRIDING - Method overriding is the method having the same name with the same arguments..
# It is implemented with inheritance also..
# It mostly used for memory reducing process..

class A:
    def displayA(self):
        print("I am in Mumbai")

class B(A):
    def displayB(self):
        print("I am in Delhi")

obj=B()
obj.displayB()