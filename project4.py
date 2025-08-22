from numpy import random



print("What do you choose?\n[1]Rock\n[2]Paper\n[3]Scissors")
choice = int(input("Type here:"))

if choice == 1:
    choice = "Rock"
elif choice == 2:
    choice = "Paper"
elif choice == 3:
    choice = "Scissors"

computerChoice = random.choice(["Rock", "Paper", "Scissors"])

print(f"You decided to play: {choice}\nThe Computer decided to play: {computerChoice}")

def winnerDecider():
    if choice == computerChoice:
        print("Tie!")
    else:
        if choice == "Rock":
            if computerChoice == "Paper":
                print("You lost!")
            else:
                print("You won!")
        elif choice == "Paper":
            if computerChoice == "Rock":
                print("You won!")
            else:
                print("You lost!")
        else:
            if computerChoice == "Paper":
                print("You won!")
            else:
                print("You lost!")

winnerDecider()


