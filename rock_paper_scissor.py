import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win"
    else:
        return "Computer wins"

print("Welcome to Rock-Paper-Scissors")

while True:
    print("\nChoose: rock, paper, or scissors")
    player_choice = input("Your choice: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("bye")
        break

