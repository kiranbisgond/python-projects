import random
choices = {
    1: "rock",
    2: "paper",
    3: "scissors"
}
user = input("Enter rock, paper or scissors: ").lower()
computer = random.choice(choices)
print("Computer:", computer)
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    print("THANKS FOR PLAYING")
