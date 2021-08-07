max = None
most = None
data = dict()
fname = input("Enter file : ")
name = None
try :
    handle = open(fname)
except :
    print("Sorry File ",fname," Not Found")
    quit()

for line in handle :
    line = line.rstrip()
    if line.startswith("From:"):
        lined = line.split()
        name = lined[1]
        data[name] = data.get(name,0) + 1

for name in data:
    if max is None:
        max = data[name]
        most = name
    elif max < data[name]:
        max = data[name]
        most = name

print(most,max)
