x=int(input("enter the value of x: "))
#x is a the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # if x is 4
    case 4:
        print("case is 4")  
 
  #case is with if-condition
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)
    



