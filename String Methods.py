# String Methods
# Strings are immutable means you cannot change the strings but you can generate a new string by its Methods 
a="sami Ullah  !!!!!!!!!!! sami"
a1="!!Sami Ullah !!!!!!!!!!!"
# len=len(a)
print(a)
print(a1)
print(a.upper()) #these are new strings and by using Methods
print(a.lower()) #Strings Cannot be changed

#rstrip method
print(a.rstrip("!"))
print(a1.rstrip("!"))

# Replace String
print(a.replace("Sami Ullah","Mughal"))
print(a1.replace("Sami Ullah","Mughal"))

#split/List method
print(a.split())

#capitilize method 
blog="iNTRoduction tO jaVAscript"
print(blog.capitalize())

# center method
str1 = "welcome to the console"
len1 = len(str1)
print(len1)
print(str1.center(50))
print(len(str1.center(50)))  # This will now work correctly

#count function/Method
print(a.count("sami"))

#ends with method
s="how are you!!!"
print(s.endswith("!"))
print(s.endswith("are", 2, 10))

#Find Method & Index Method
q="he's name is Sami.he is an honest man"
print(q.find("is"))
print(q.find("ishi"))
print(q.index("is"))


# isalnum Method
h="welcometoconsole000"
h1="how are you \n"
print(h.isalnum())    #A-Z,a-z,0-9
print(h.isalpha())    #A-Z,a-z
print(h.islower())    #letters is lowercase
print(h1.isprintable())   

#isspace Method
str="       " #using space
print(str.isspace())

str="       " #using Tab
print(str.isspace())
#Title Method
str="Sami Ullah Mughal"
print(str.istitle())

#startwith
str="python is a Roadmap to Agentic AI"
print(str.startswith("python"))

#swap case lower to uppercase and vice versa
str="Python is a Roadmap to Agentic AI"
print(str.swapcase()) 

str="he's name is Sami.he is an honest man"
print(str.title())

