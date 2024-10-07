print("Welcome to the treasure Game")
name = input("Enter your name? \n")
choice1 = input("so "+name+" right or left (L or R)\n")
if choice1 == "L":
    choice2 = input("you have reached a lake, there is a island in the middle of the lake. \n"
                    "Type 'wait' to wait for the boat or type 'swim' to swim across \n").lower()
    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed. there is a house with 3 doors, one red, one blue and one yellow"
                        "which color do you choose \n")
        if choice3 == "red":
            print("it's a room full of fire. game over")
        elif choice3 == "yellow":
            print("you found the treasure you win")
        elif choice3 == "blue":
            print("you enter a room of beasts.. Game over")
        else:
            print("you chose a door that doesn't exist")
    else:
        print("you got attacked by a shark and you died. game over")
else:
    print("you fell into a whole.. game over")



