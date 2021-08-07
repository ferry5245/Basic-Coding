fname = input("Enter File Name : ")
count = 0
try:
    fh = open(fname)
except:
    print("Sorry Couldn't Find Appointed File Named", fname)
    quit()

for line in fh:
    line = line.strip()
    if line.startswith("From:"):
        temp = line.split()
        print(temp[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
