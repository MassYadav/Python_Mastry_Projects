# fake news headline generator
import random
subjects = ["Aliens", "Scientists", "Politicians", "Celebrities", "Robots"]
verbs = ["discover", "invent", "steal", "destroy", "save"]
objects = ["a new planet", "a cure for a disease", "a secret plan", "a powerful weapon", "a hidden treasure"]
while True: 
    subject  = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    headline = f"{subject} {verb} {object}!"
    print(headline)
    play_again = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if play_again != "yes":
        break


print("Thanks for using the fake news headline generator! Goodbye!")    