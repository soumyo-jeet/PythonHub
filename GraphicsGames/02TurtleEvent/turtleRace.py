import turtle
import random
my_screen= turtle.Screen()
turtles = ['blue','red','yellow','green','black']

my_screen.setup( width= 500, height= 600)
bet = my_screen.textinput(title="Put Your Bet:", prompt="Choose a color in (blue/red/yellow/green/black)")

y = 200
racers = []
for each in turtles:
    t = turtle.Turtle('turtle')
    t.penup()
    t.color(each)
    t.goto(-245 , y)
    y -= 100
    racers.append(t)

game_over = False
win = ""
while not game_over :
    for t in racers:
        if t.xcor() > 245:
            win = t.fillcolor()
            game_over = True
            break
        random_dist = random.randint(0,10)
        t.forward(random_dist)
    
    
if bet == win :
    print(f"{win.capitalize()} won the race. You got your bet!")
else:
    print(f"{win.capitalize()} won the race. You loose your bet!")



          
    










my_screen.exitonclick()