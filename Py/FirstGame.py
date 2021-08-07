print("My First Game!!!")

name = input("Please Tell Me Your Name : ")
age = int(input("Your Age Please : "))
health = 10
print("Welcome to my game, %s. Your age is %d years old" %(name,age))
if age >= 18:
    wanna_play = input("Hey, you're allowed to play!!! Would you like to play with me? ").lower()
    if wanna_play == "yes":
        print("Let the Game Begin!")
        weapon = None
# Decides Where to go
        d_first_decision = input("You see a dungeon at your left side, and an old mansion on your right side, which way would you like to go (left/right)? ").lower()
        if d_first_decision == "left":
            # Opening Chest
            ans = input("You see a chest, would you like to open it (yes/no)?").lower()
            if ans == "yes":
                print("You have opened the chest!!! There's some weapon in it, ")
                weapon = int(input("1. Sword\n2. Bow(1 arrow)\n3. Hammer\nWhat will you choose (1,2,3)? "))
                wpn = ["sword","bow","hammer"]
                weapon = wpn[weapon-1]
                print("You have taken the",weapon)
            else: print("You leave the chest alone...")
            print("You are entering the dungeon...")
# Meeting with mr. Rock
            d_second_decision = input("You see a big rock ahead, would you like to hit it (yes/no)? ")
            if d_second_decision == "yes" and weapon == "hammer" :
                print("You have destroyed the rock, but the hammer is broken...\n")
                armed = None
            elif d_second_decision == "yes" and not weapon == "hammer" :
                print("Sorry You can't destroy the rock...\nYou are going to look what's around...\n")
                # Spider's Den
                print("You see a sleeping giant spider ahead...")
                spider = input("Will you sneak around the spider or attack it (sneak/attack)? ").lower()
                if spider == "sneak":
                    print("You snuck around it safely...")
                elif spider == "attack" and weapon == "bow" :
                    print("You killed the spider safely, but your arrow broken, the bow is useless now...")
                    weapon = None
                elif spider == "attack" and weapon == "sword":
                    health = health - 5
                    print("You attacked the spider and lose %d health" %(health))
                else:
                    print("The spider killed you...")
                    health = 0
# Health check
                if health == 0:
                    print("You lost the game")
                    quit()
                else:
                    print("You pass the Spider's Den...\n")
                    # Fountain
                    fountain = input("You see a fountain ahead, would you like to take a sip (yes/no)? ").lower()
                    if fountain == "yes":
                        health = 10
                        print("Your health replenished, health is",health)
                    else : print("You feel cautious and leave the fountain")
                print("You leave the fountain\n")
                # Chasms
                

            else :
                print("You leave the rock alone...\nYou are going to look what's around")
                print("You see a sleeping giant spider ahead...")
                spider = input("Will you sneak around the spider or attack it (sneak/attack)? ").lower()
                if spider == "sneak":
                    print("You snuck around it safely...")
                elif spider == "attack" and weapon == "bow" :
                    print("You killed the spider safely, but your arrow broken, the bow is useless now...")
                    weapon = None
                elif spider == "attack" and weapon == "sword":
                    health = health - 5
                    print("You attacked the spider and lose %d health" %(health))
                else:
                    print("The spider killed you...")
                    health = 0

                if health == 0:
                    print("You lost the game")
                    quit()
                else:
                    print("You pass the Spider's Den...")
                    fountain = input("You see a fountain ahead, would you like to take a sip (yes/no)? ")
                    if fountain == "yes":
                        health = 10
                        print("Your health replenished, health is",health)
                    else : print("You feel cautious and leave the fountain")



        elif first_decision == "right":
            print("You are entering the old mansion... You started to have a bad feelings about it...")
            m_second = input("You see stairs on the left and a gloomy room in the right, where will you go (left/right)?")
    else :
            print("See you later, then")
else :
    print("Sorry you are not old enough to play")
