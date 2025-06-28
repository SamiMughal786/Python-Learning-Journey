#make calculator by using user input & Type Casting   

## Step 1: Take input as strings
x=input("Enter the first Number: ")
y=input("Enter the second Number: ")

# Step 2: Convert input to integers
num1=int(x)
num2=int(y)

# Step 3: Perform calculation
print("the sum of",x, "+", y, "is:", num1+num2)
print("the sub of",x, "-", y, "is:", num1-num2)
print("the Div of",x, "/", y, "is:", num1/num2)
print("the Mul of",x, "*", y, "is:", num1*num2)