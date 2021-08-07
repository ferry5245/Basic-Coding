greet="Hello, World"
print(greet)
gender=input("Are you a Male or Female? ")
name=input("Input your name: ")
length=len(name)
draft=greet[:6]
if(gender=="Male"):
    greeting=draft + " Mr. " + name
elif(gender=="Female"):
    greeting=draft + " Mrs. " + name
else: print("Error!!!")
print(greeting)
