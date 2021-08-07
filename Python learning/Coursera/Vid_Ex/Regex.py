import re
total = 0

fname =  input("File Name : ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if re.findall('[0-9]+',line):
        list = re.findall('[0-9]+',line)
        for nums in list:
            nums = int(nums)
            total += nums

print(total)
