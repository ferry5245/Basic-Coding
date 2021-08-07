def computepay(a,b):
    if(a<40):
        pay=a*b
    else:
        pay=(a-40)*(b*1.5)+40*b
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
