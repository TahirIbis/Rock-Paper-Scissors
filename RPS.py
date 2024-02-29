import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, scissors, lizard, or spock: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, scissors, lizard, or spock.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

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

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

def play_game():
    print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
    while True:
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    print("Thanks for playing!")

play_game()


