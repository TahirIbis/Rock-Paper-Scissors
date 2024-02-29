import random

# Function to get the user's choice with input validation
def get_user_choice():
    while True:
        # Prompt the user for their choice
        user_choice = input("Choose rock, paper, scissors, lizard, or spock: ").strip().lower()
        # Validate the user's input
        if user_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
            return user_choice
        else:
            # If input is invalid, prompt the user to choose again
            print("Invalid choice. Please choose rock, paper, scissors, lizard, or spock.")

# Function to get the computer's choice
def get_computer_choice():
    # Randomly select a choice for the computer
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

# Function to determine the winner based on choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'spock' or computer_choice == 'paper')) or \
         (user_choice == 'spock' and (computer_choice == 'scissors' or computer_choice == 'rock')):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a single round of the game
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Function to play the entire game
def play_game():
    print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
    while True:
        play_round()
        # Ask the user if they want to play another round
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            # If the user doesn't want to play again, exit the loop
            break
    # Thank the user for playing once the game is over
    print("Thanks for playing!")

# Start the game
play_game()



