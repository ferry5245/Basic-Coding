largest = None
smallest = None
invalid = -1
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        n = int(num)
        if smallest is None and largest is None:
            smallest = n
            largest =  n
        elif n < smallest :
            smallest = n
        elif n > largest :
            largest = n
    except:
        invalid = 0

if invalid==0:
    print("Invalid Input")
print("Maximum is", largest)
print("Minimum is", smallest)
