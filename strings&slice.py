# Strings In Python
name='Sami Ullah'
print("Hello, " + name)

#Multiline Strings in this method
Chat='''he said
i am good 
how are you?
What are you Doing right now'''
print(Chat)

# Assessing characters of a string by using Index
index="SAMI"
print(index[0])
print(index[1])
print(index[2])
print(index[3])

# Assessing multiline string using for loop
for characters in Chat:
    print(characters)


#String Slicing & Operations on string
# Find length of a string
fruit="mango"
len1=len(fruit)
print("Mango is a", len1,"letter word")

#String Slicing
fruit1="Apple"
len=len(fruit1)
print(fruit1[0:3])
print(fruit1[0:6])
print(fruit1[0:1])
print(fruit1[-1:3])
print(fruit1[-3:-1])

#Quick #Quiz
nm="Harry"
print(nm[-4:-2])

