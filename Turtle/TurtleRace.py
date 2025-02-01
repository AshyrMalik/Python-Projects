import turtle
from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500,height=400)

colors=["red","orange","blue","purple","green","black"]
y_coordinate = 150
turtles=[]
for color in colors:
    timm = Turtle(shape="turtle")
    timm.penup()
    timm.color(color)
    timm.goto(x=-230,y=y_coordinate)
    y_coordinate-=60
    turtles.append(timm)


user_guess = screen.textinput(title="Make the bet",prompt="Select the color for the turtle you think will win the race")
print(f"User bet on: {user_guess} turtle")
start_race=False
if user_guess:
    start_race= True

while start_race:

    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor()==user_guess:
                print(f"Your {turtle.pencolor()} turtle has won the race")
                start_race=False
                break
            else:
                print(f"{turtle.pencolor()} turtle won the race! You lost the bet")
                start_race = False
                break

        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
