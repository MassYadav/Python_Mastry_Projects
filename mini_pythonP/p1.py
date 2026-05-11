import random
def roll():
    min_value =1
    max_value = 6
    return random.randint(min_value, max_value)
print("Welcome to the dice roller!")
while True:
    players = input("Enter the number of players (2 - 4) ")
    if players.isdigit():
        players  = int(players)
        if players < 2 or players > 4:
            print("Please enter a number between 2 and 4.")
        else:
            break
    else:
        print("Please enter a valid number.")

print(f"Rolling the dice for {players} players...") 

max_score = 0
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for players_idx in range(players):
        print(f"\nPlayer {players_idx + 1}'s turn:")
        current_score = 0
        while True:
            should_roll = input("Do you want to roll the dice? (yes/no) ").lower()
            if should_roll != "yes":
                print("Thanks for playing! Goodbye!")
                exit()
            roll_result = roll()
            if roll_result == 1:
                print("Oh no! You rolled a 1. Your score resets to 0.")
                current_score = 0
                break
            else:
                current_score += roll_result
                print(f"Your current score is {current_score}.")
                print(f"You rolled a {roll_result}!") 
        players_score[players_idx] += current_score
        print(f"Player {players_idx + 1}'s total score is {players_score[players_idx]}.")
        if players_score[players_idx] > max_score:
            max_score = players_score[players_idx]
            print(f"Player {players_idx + 1} takes the lead with a score of {max_score}!")             