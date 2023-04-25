#Polimorphism...means same function name (but different signatures) being uses for different types...something occure in several form.
  #1.-function overloading
  #2.-function overriding

l=[12,34,54,23]
print(len(l))
s=("blue","orangr","red","green","black")
print(len(s))


# 1.-Function Overloading....where function name is same but output/return will be different
class Ws:
    def display(self,name=" "):
        print("welcome to India" + name)

obj=Ws()
obj.display()           #here we did not pass the the argument (name) value
obj.display("Rahul")    #here we pass the argument value



# 2.-Function Overriding ...same name with same argument...when we inherite same function then child function override the parent function.
class Ws:
    def display(self):                 #parent function
        print("welcome to India")

class IIT(Ws):                         #here IIt inherite Ws       
    def display(self):                 #child function
        super().display()       #super() function is used to call parent function when both function is same
        print("Welcome my Champ")

obj=IIT()             #...for avoiding ovverriding we use super() function
obj.display()         #according to inheritance concept parent charecter come in chlld...it will overriding.




   

    