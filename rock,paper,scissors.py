import random
print("Script Running...")
player_choice = input("Choose rock, paper, or scissors: ").lower()
choices = ("rock","paper","scissors")
computer_choice = random.choice(choices)
print("Let's play Paper, Rock, Scissors")
print(f"Computer Chose: {computer_choice}")
print(f"Player Chose: {player_choice}")
if ((player_choice == "rock" and computer_choice == "scissors") 
    or (player_choice == "scissors" and computer_choice == "paper") 
    or (player_choice == "paper" and computer_choice == "rock")):
    winner = "user"
elif player_choice == computer_choice:
    winner = "Tie"
else:
    winner = "Computer"
print(f"The winner is {winner}")
if winner == "Player":
    print("You Won!")
elif winner == "Computer":
    print("Computer Won")
else:
    print("It's a Tie!")

def main():
    print("Script Complete")

if __name__ == "__main__":
    main()