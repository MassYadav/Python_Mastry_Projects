import random 
easy = ["cat","dog","mouse","bird","fish"]
medium = ["elephant","giraffe","dolphin","kangaroo","penguin"]
hard = ["hippopotamus","rhinoceros","chimpanzee","orangutan","alligator"]
print("Welcome to the Word Guessing Game!")

level = input("Choose a difficulty level (easy, medium, hard): ").lower()
if level == "easy":
    secret = random.choice(easy)
elif level == "medium":
    secret = random.choice(medium)
elif level == "hard":
    secret = random.choice(hard)    
else:
    print("Invalid level. Defaulting to easy.")
    secret = random.choice(easy)
attempt = 0;
while True: 
    guess = input("Guess the secret: ").lower()
    attempt += 1
    if guess == secret:
        print(f"Congratulations! You guessed the secret in {attempt} attempts!")
        break
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")

print("Thanks for playing the Word Guessing Game! Goodbye!")