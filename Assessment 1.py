import random

def play_game():
    # Step 1: Define possible choices
    choices = ["rock", "paper", "scissors"]

    # Step 2: Get user choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please pick rock, paper, or scissors.")
        return

    # Step 3: Generate computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Step 4: Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
play_game()