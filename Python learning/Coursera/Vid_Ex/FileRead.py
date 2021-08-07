fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Sorry, unable to read file or it doesn't exists.")
    quit()

x = 0
total = 0
num = 0
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find("0")
    num = float(line[pos:])
    x+=1
    total = total + num
    print(line)
print("Average spam confidence:", total/x)
