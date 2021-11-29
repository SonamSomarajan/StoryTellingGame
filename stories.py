"""
This is my very first Python game on the lines of Dungons and Dragons.
I intend to create this game to practice the basic concepts of Python.
Let's see how this goes.
"""
import os

#Function for going East:
def east():
    print("\nAs you walk, you realize that the jungle is thinning out, paving way for a village settlement.\nThe sun is starting to set.")
    print("The forest prepared you well due to the low availability of sunlight in it.")
    print("\nWould you like to:\n 1. Go to the settlement? \n 2. Hide in the bushes and wait till nightfall so that nobody discovers you?\n")
    choice = input("(Go/hide)").lower()
    while True:
        if choice == "hide":
            print("As the night approaches, you slowly fall asleep. \nA black mamba, a very poisonous snake, bites you and you die.")
            break
        elif choice =="go":
            print("On reaching the settlement, you are given a warm welcome.\n Suddenly, a siren goes off.\n\nThe Naxals are coming to rampage the village.\n")
            print("Do you fight the terrorists or hide?")
            while True:
                choice = input("(fight/hide)").lower()
                if choice == "hide":
                    print("\nYou are discovered by one of the terrorists and killed.\n")
                    return("lost")
                    break
                elif choice == "fight":
                    print("The villagers are fed up of the terrorists too. \nThey pick up their arms and fight along with you.\n")
                    print("You win the fight and become the protagonist of the village!\n")
                    print("\nCongratulations!!!\nYou have won this quest")
                    return ('won')
                    break
                else:
                    print("\nInvalid input. Try again.")
                    continue
        else:
            print("\nInvalid input. Try again.")
            continue


#Function for going west:
def west():
    print("\nA very hungry tiger appears before you. \nWould you like to fight it or run for your life?")

    choice = input("(f/r)").lower()
    if choice == "f":
        print("The tiger kills you. You are now the tiger's dinner feast.")
        #break
    elif choice == 'r':
        print("\nYou realize the tiger is very fast.\nWould you like to climb a tree or continue running?")
        while True:
            choi = input("(c/r)").lower()
            if choi == "c":
                print("\nThe tiger can climb the tree faster than you. \nIt kills you and you die.\n")
                break
            elif choi == "r":
                print("\nYou frantically start running towards the east. You slowly lose the tiger.")
                east()
                break
            else:
                print("\nInvalid input. Try again.")
                continue
        #break
    else:
        print("Invalid input. Try again")
        #continue


    return("lost")

#Exploring the forest.
def explore():
    print("\nYou continue exploring the forest. \nSuddenly, an arrow flies very close to your eye and strikes the tree nearby.")
    print("\nOn looking up, you see a tribal man trying to kill you with a poisonous arrow.")
    print("Do you fight him or run for your life?\n")

    while True:
        choice = input("(f/r)").lower()
        if choice == "f":
            print("You are killed by the tribal man. He ties you up and takes you to his settlement for a feast.\n")
            break
        elif choice == "r":
            print("\nYou frantically start running east. \n")
            east()
            break
        else:
            print("Invalid choice. Try again.")
            continue
    return("lost")

#The function north tells what happens on moving north
def north():
    print("\nOn going north, you see an old man meditating under the shade of a banyan tree.\nA deer nearby stomps the ground hard, startling the man. \nWould you like to talk or walk away to escape from the man?\n")
    choice = input("(t/w)").lower()
    if choice == "w":
        explore()
    elif choice == "t":
        print('The man says, "You are in a place infested with Naxalism.\nThey are a very dangerous terrorist outfit.\nYour life is in danger".\n')
        print('"My advice to you would be to escape the jungles as soon as possible.\nMove east at the earliest."')
        print("Would you trust him and move east or explore the jungle?")
        while True:
            choice = input("(move/explore)").lower()
            if choice == "explore":
                explore()
                break
            elif choice == "move":
                east()
                break
            else:
                print("Invalid input. Try again.")
                continue

#The start function is the where the game begins
def start():
    os.system("cls")
    print("\nYou find yourself in the thick jungle of Dandakaranya, located in Orissa, \ncentral India, after being thrown out of a plane. \n")
    print("Tall trees, shooting towards the sky, surroung you. \nTheir canopy is so thick that very little sunlight reaches the ground. \nThe thick undergrowth helped cushion your fall.\n")
    print("You are bruised, Yet, alive. On standing up, the undergrowth reaches your knees.\n What direction would you like to travel, north, south, east or west?\n")

    while True:
        direction = input("Enter (n/e/w/s)").lower()
        if direction == "n":
            north()
            break
        elif direction == "s":
            print("\nYou accidentally walk into a ditch covered in the undergrowth. \nYou scream. But, nobody hears you. \nYou die in pain, thirst and hunger.\n")
            break
        elif direction == 'e':
            east()
            break
        elif direction == 'w':
            west()
            break
        else:
            print("Wrong input.")
            continue

"""
The first function, "intro", accepts the player's name and age.
It checks if the person is above 18 years and allows to player
to play only if he/she is above the age of 18.
"""

def intro():
    name = input("Enter your name.")
    age = input("Enter your age.")
    age = int(age)
    if age >= 18:
        print("Hello,", name+". \nYou are old enough to play.")
        key = input('\nPress any key to continue. \nType "exit" to exit.').lower()
        if key == "exit":
            return
        start()
    else:
        print("Hello,", name+". You are very young to play. Sorry.")

#This is the control function. It decides the direction of the game.
def control(stat ="lost"):
    intro()
    if stat =="won":
        print(" *** YOU WIN!!! ***")
    else:
        print("\nGAME OVER!!!")

#This is where the magic starts:
os.system("cls")
print("\nHello and welcome to my very first Python game. \nThis is a game driven by your imagination. \n")
key = input("Press any key to start.")
os.system("cls")
control()
while True:
    key = input("\nWould you like to play again?\nType 'exit' to exit.").lower()
    if key == "exit":
        break
    else:
        control()
