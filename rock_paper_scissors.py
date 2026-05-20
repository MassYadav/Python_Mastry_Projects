import random
print("Welcome to the Rock, Paper, Scissors game!")
user_win = 0
computer_win = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_input == "quit":
        print("Thanks for playing! Goodbye!")
        break
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_win += 1
    else:
        print("You lose!")
        computer_win += 1

print(f"Final Score - You: {user_win}, Computer: {computer_win}")