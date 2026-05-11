import random
print("Welcome to the number guessing game!")
top_of_range = input("Enter the upper limit for the number to guess: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a positive number next time.")
        exit()
else:
    print("Please enter a valid number next time.")
    exit()

number_to_guess = random.randint(0,top_of_range)

attempt = 0;
while True: 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter the number next time.")  
        continue
    attempt += 1
    if user_guess == number_to_guess:
        print("Congratulations! You guessed the number.")
        break 
    elif user_guess < number_to_guess:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")    
print(f"You made {attempt} attempts.")           