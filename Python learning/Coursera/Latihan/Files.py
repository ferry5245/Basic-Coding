def reading(handle):
    handle = open("File.txt","r")
    for fil in handle :
        print(fil)
    handle.close()

#def main():


if __name__ == "__main__":
    fh = open("File.txt","w")
    x = list()
    n = int(input("How many data? "))
    for num in range(n) :
        data = input("Add Name : ")
        x.append(data)
    sorted(x)
    for dat in range(n):
        fh.write(x[dat])
    fh.close()
    reading(fh)
