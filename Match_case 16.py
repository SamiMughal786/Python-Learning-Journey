# Matc case statement 

x=int(input("Enter you value of x: "))

match x:
    case 0:
        print("the case is zero")
    case 1:
        print("the case is one")
    case 2:
        print("the case is two")
    case 3:
        print("the case is three")
    case 4:
        print("the case is four")
    case _:
        print(x)

# Use of If statement in match case

x=int(input("enter the value: "))
match x:
    case 0:
        print("the case is zero")
    case 1:
        print("the case is one")
    case 2:
        print("the case is two")
    case _ if x==25:                #use of if statement in match case statement
        print("the case is 25")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")

# Example
x =int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)