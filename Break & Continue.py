#Break & Continue statement in python
#Break statement
for i in range(12):
    if(i==10):
        break
    print("5 x ", i+1, "=", 5 * (i+1))

print("come out from the loop")

#Continue Statement
for x in range(20):
    if(x==12):
        print("Come out from ietration")
        continue
    print("2 x", x+1, "=", 2*(x+1))


#Break statement Example
for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("Hello World")
print("Thank You")

#Continue Example
for i in [2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)