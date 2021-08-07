largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    try:
        n=float(num)
        
    except:
        print("Invalid input")
        continue

    if num == "done" : break


print("Maximum", largest)
print("Minimum", smallest)
