# # Conditional operators
# # <, >, <=, >=, ==, !=
# # If Else Conditional Statement
age=int(input("Enter your Age: "))
print("Your Age is: ", age)

if(age>=18):
    print("You Can Drive the Car")
else:
    print("You Cannot Drive the Car")

#Second Example
Appleprice=210
budget=200
if(Appleprice<=budget):
    print("Alexa, add 1 kg apples in the cart")
else:
    print("Alexa, do not add apples in the cart")

# elif statement 
num=int(input("Enter the value of number: "))
if(num<0):
    print("The number is negative")
elif(num == 0):
    print("The number is Zero")
elif(num == 786):
    print("The number is special")
else:
    print("The number is positive")
print("Oh it will working")

# nested if statement

num=18
if(num<0):
    print("the number is negative")
elif(num>0):
    if(num<=10):
        print("the is less than 10")
    elif(num>10 and num<=20):
        print("the number is between 11 and 20")
    else:
        print("the number is greater than 20")
else:
    print("Number is zero")

