lists = list()
lined = None
fname = input("Insert File Name Here : ")

try:
    fh = open(fname)
except:
    print("File not found")
    quit()

for line in fh:
    line = line.strip()
    lines = line.split()
    for data in lines:
        if not data in lists:
            lists.append(data)

lists = sorted(lists)
print(lists)
