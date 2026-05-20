import turtle 
import time
import random
WITDTH ,HEIGHT = 500,500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def race(colors):
    turtles = create_turtule(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]
            


def create_turtule(colors):
    turtles  = []
    spacingx  = WITDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WITDTH//2 + (i+1) * spacingx ,- HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles    

def init_turtule():
    screen = turtle.Screen()
    turtle.setup(WITDTH,HEIGHT)
    screen.title("Racer Game")

def get_number_of_recers():
    while True:
        racer = input("Enter number of racers (2-10): ")
        if racer.isdigit():
          reacer = int(racer)
        else:
           print("Please enter a valid number.")
           continue
        if 2 <= reacer <= 10:
            return reacer   
        else:
            print("Please enter a number between 2 and 10.")


racers = get_number_of_recers()
init_turtule()

random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)
winner =  race(colors)
print("The winner is color : ",winner)
time.sleep(5)