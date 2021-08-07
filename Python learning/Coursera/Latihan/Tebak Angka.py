import random
import time

def main():
    life = 3
    print("Tebak Angka (0-20)")
    num = number()
    check(num)

def number():
    return random.randrange(0,20)

def check(numbers):
    cek = False
    life = 2
    print("What is the Number?")
    print("Life left :", life+1)
    while cek == False and life >= 0:
        guess = input(">>> ")
        try:
            inp = int(guess)
        except:
            print("Sorry, Bad Input")
            life -= 1
            print("Life left :", life+1 , "\n")
            continue
        if life == 0:
            print("Sorry You Lost")
            break
        elif inp > numbers:
            print("Too High")
            life -= 1
            print("Life left :", life+1 , "\n")
            continue
        elif inp < numbers:
            print("Too Low")
            life -= 1
            print("Life left :", life+1 , "\n")
            continue
        else :
            print("Congratulations!!! The Number is",numbers)
            print("Life left :", life+1 , "\n")
            cek = True
    time.sleep(3)

if __name__ == "__main__":
    main()
