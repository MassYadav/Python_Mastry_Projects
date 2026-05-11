print("Welcome to the quiz game!")
user = input("Do you want to play? (yes/no) ")

if user.lower() != "yes":
    print("Maybe next time. Goodbye!")
    exit()
print("Great! Let's get started.")
score = 0
answer = input(" What is the cpu stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is central processing unit.")\

answer  = input(" What is the ram stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else :
    print("Incorrect. The correct answer is random access memory.")

answer = input(" What is the gpu stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect. The correct answer is graphics processing unit.")

print(f"Your final score is {score}/3.")