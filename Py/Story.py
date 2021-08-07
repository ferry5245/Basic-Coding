def study():

def hardest_time():

def bitter_love():


print("Hello, User...")
name = input("Can you tell me your name, please?")
age = int(input("What is your age, friend?"))

ask = input("Do you want to know my story (yes/no)? ").lower()
if ask == "yes":
    genre = input("1. Study\n2. Hardest Time\n3. Bitter Love\nWhat story do you prefer (1,2,3)? ")
    lists = ["study","Hardest Time","Bitter Love"]
    genre = lists[genre-1]
    print("You have chosen the ",genre," genre")
