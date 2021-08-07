def count(a,b):
    counting=int(0)
    i=int(0)
    for i in a:
        if i==b:
            counting+=1
    return counting


sentence = input("Input your word here : ")
letter = input("What letter do you look for? ")
found=count(sentence,letter)
print("The sentence has %d letter %s" %(found,letter))
