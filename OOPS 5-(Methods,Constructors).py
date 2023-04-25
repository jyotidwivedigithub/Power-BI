# Method and Constructors of Object Oriented Programming(OOPs)
   #Method-
   #Constructor {def __init__(self)} -is like a method doesn't need to call--
   # - it is automatically called method.if any thing define in constructor can also used in other function

class DemoClass:
    a=10
    def __init__(self):            #self is a key/used as object we can use anything else in place of self
        print("Welcome to World")

    def showvalue(self):
        #print(a)         #return error because here a will be defined by self
        print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome zain")

    def showvalue2(self,a,b):   #self is used with argument(a,b)
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(12,11)


class DemoClass:
    a=30
    def __init__(self):
        print("Welcome to Delhi")

    def showvalue(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,34)


