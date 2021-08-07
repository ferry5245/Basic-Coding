data = 'From ferrychandra@telkomuniversity.ac.id Sat Feb 5 09:14:16 2021'
# Find the position of "@"
atpos = data.find("@")
print(atpos)
# Finding the end of host's position
sppos = data.find(" ",atpos)
print(sppos)
# From the @ position+1 to end of host position
host = data[atpos+1:sppos]
print(host)

atposA = data.find(" ")
print(atposA)
spposA = data.find(" ",atposA+1)
print(spposA)
sender = data[atposA+1:spposA]
print(sender)
