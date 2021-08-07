#A=("Hello World!!")
#print(A)

#name=input("Input Your Name : ")
#print("Hello, %s"%name)

#print(12>=12.0)



#age=int(input("Please type your age here : "))
#if(0<age and age<=16):
#    print("You are unable to create national ID")
#elif(0<age and age>16):
#    print("You are able to create national ID")
##else:
#    print("Invalid age")

age=int(input("How is your age : "))
confirm=input("Do you have a driving license (Yes/No)? ")
if(age>0 and age<=17):
    print("You are unable to drive this vehicle")
elif(age>0 and age>17 and confirm=="No"):
    print("You are unable to drive this vehicle")
elif(age>0 and age>17 and confirm=="Yes"):
    print("You are able to drive this vehicle")
else:
    print("Invalid Input")