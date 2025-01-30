from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def move_forward():
    timmy.forward(100)

def move_backward():
    timmy.backward(100)

def turn_clockwise():
    timmy.left(90)
def turn_anti_clockwise():
    timmy.right(90)



screen = Screen()
screen.listen()
screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= move_backward)
screen.onkey(key='d',fun=turn_clockwise)
screen.onkey(key='a',fun=turn_anti_clockwise)
screen.exitonclick()
