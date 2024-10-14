import random
print("Welcome to Rock Paper Scissors!")

name = input("Enter your name: ")
element = ["Rock", "paper", "scissors"]

#computerelement will randomly choose an index from the element list and it will be stored in computer_elements
computer_element = element[random.randint(0,2)]

#the user is going to choose an index from the elements list and stores it in your_element
your_element = element[int(input(name+" "+" Choose an element (0 for rock, 1 fpr paper and 2 scissors)"))]

if your_element == computer_element:

    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" it's a tie")
    
elif your_element == "Rock" and computer_element == "paper":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you lose")

elif your_element == "Rock" and computer_element == "scissors":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you win")
elif your_element == "paper" and computer_element == "scissors":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you lose")

elif your_element == "paper" and computer_element == "rock":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you win")
elif your_element == "scissors" and computer_element == "paper":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you win")
elif your_element == "scissors" and computer_element == "rock":
    print(name+" you chose"+" "+your_element+" and the computer chose "+computer_element+" you lose")

