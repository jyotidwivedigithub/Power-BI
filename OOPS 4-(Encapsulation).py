#Encapsulation(private)--an object variables should not always be directly accessible..
# it means we can use variable in class but not outside of class
# The method can ensure the correct values are set.If an incorrect value is set, the method can return an error.

class Student:
#     __name="Ravi"            #it is private variable define by underscora__
#obj=Student()   
#print(obj.__name)             return error because private variable cannot be directly used by object

      __name="Ravi"            #it is private variable define by underscora__
      def __init__(self):
        print(self.__name)
      
      def __display(self):     #it is also a private variable__   
        print("Welcom to India")

obj=Student()   
obj.__display()      