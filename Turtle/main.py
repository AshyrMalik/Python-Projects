from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
#
#
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

def move_forward():
    timmy.forward(100)




screen = Screen()
screen.listen()
screen.onkey(key="space",fun= move_forward)
screen.exitonclick()
