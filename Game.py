#Brian Imfeld   10/25/11
import random

print ("\t\t Cave of Caerbaggon ")
print ("Directions: Select your weapon and hope for the best.")

score = 0
lives = 5

while lives > 0:
    
    print ("1)Sword")
    print ("2)Dagger")
    print ("3)Lance")
    print ("4)Mace")
    print ("5)The Holy Handgrenade of Antioch")

    weapon = int(input("Please choose your weapon:"))
              
    x = random.randrange(10)


    if weapon == 1:
        if x <= random.randrange(10):
            print("You killed the rabbit!")
            score = score + 500
            lives = lives + 1
        else:
            print("You're Dead!")
            lives = lives - 1
            score = score - 300


    elif weapon == 2:
        if x <= random.randrange(10):
            print ("You killed the rabbit!")
            score = score + 400
        else:
            print ("You're dead!")
            lives = lives - 1
            score = score - 200


    elif weapon == 3:
        if x <= random.randrange(10):
            print ("You killed the rabbit!")
            score = score + 300
        else:
            print ("You're dead!")
            lives = lives - 1
            score = score - 100


    elif weapon == 4:
        if x <= random.randrange(10):
            print ("You killed the rabbit!")
            score = score + 200
        else:
            print ("You're dead!")
            lives = lives - 1
            score = score - 100
        
 
    elif weapon == 5:
        if x < random.randrange(10):
            print ("You killed the rabbit but lost a life!")
            score = score + 400
            lives = lives - 1
        else:
            print ("You're dead!")
            lives = lives - 1
            score = score - score


    elif weapon >= 5:
        print ("Invalid weapon selecction, Repick a weapon.")

    print ("\tScore =", score)
    print ("\tLives =", lives)
