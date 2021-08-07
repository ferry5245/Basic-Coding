def main():
    x = input("Add Number Here : ")
    y = input("Add Another : ")
    inp = input("Menu:\na. Addition\nb. Subtraction\nc. Division\nd. Multiplication\nWhat do you want to do? ")
    if inp == "a" : out = adding(x,y)
    elif inp == "b" : out = subtrct(x,y)
    elif inp == "c" : out = divis(x,y)
    elif inp == "d" : out = multi(x,y)

    print("The output is ", out)

def adding(a,b):
    c = int(a)+int(b)
    return c

def subtrct(a,b):
    c = int(a)-int(b)
    return c

def divis(a,b):
    c = int(a)/int(b)
    return c

def multi(a,b):
    c = int(a)*int(b)
    return c

if __name__ == "__main__":
    main()
