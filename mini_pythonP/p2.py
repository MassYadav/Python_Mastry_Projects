with open("p2.txt", "r") as f:
    lines = f.read()


words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i ,char in enumerate(lines):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
 
        words.add(lines[start_of_word:i+1])
        start_of_word = -1

print(words)  

answers = {}
for word in words:
    answer = input("ENter word for " + word + ": ")
    answers[word] = answer

for word in words:
    lines = lines.replace(word, answers[word])

print(lines)

