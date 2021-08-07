#Latihan 1
valid=0
day=input("Please Input a day (1st word capital) : ")
days_list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(0,len(days_list),1):
    if(day==days_list[i]):
        valid=1
        x=i
        break
if(valid==1):
    print("Your day is ",days_list[x],"\nand ",days_list[x]," is the day %d"%(x+1))
else:
    print("Sorry We Couldn't Find the Day")
