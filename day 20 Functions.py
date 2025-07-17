# Functions in Python
# Function Definition
def calculate_sum(a,b): #these are parameters in Brackets
    sum=a+b
    print(sum)

    #Function Call
calculate_sum(12,2)  #these are arguements in Brackets

calculate_sum(10,44)


def print_hello():
    print("hello")

output=print_hello()
print(output) #None

#Average of 3 numbers

def average_num(a,b,c):
    avg=(a+b+c)/3
    print(avg)

average_num(1,2,3)