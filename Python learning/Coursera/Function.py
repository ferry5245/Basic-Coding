def main():
    x = input("Add Number Here : ")
    y = input("Add Another : ")
    z = adding(x,y)
    print("The sum is",z)

def adding(a,b):
    c = int(a)+int(b)
    return c

if __name__ == "__main__":
    main()
