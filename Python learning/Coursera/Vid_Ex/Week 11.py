fname = input("Enter file : ")
handle = open(fname)
lists = list()
data = dict()
datas = dict()
k = None
v = None

for line in handle :
    line = line.rstrip()
    if line.startswith("From "):
        #print(line)
        pos = line.find(":")
        name = line[pos-2:pos]
        data[name] = data.get(name,0) + 1
        #lists.append(name)

for k,v in data.items():
    temp = (k,v)
    lists.append(temp)

lists = sorted(lists)
for k,v in lists:
    print(k,v)
