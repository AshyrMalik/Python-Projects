from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.left(90)

    def go_up(self):
        new_ycor = self.ycor()+MOVE_DISTANCE
        self.goto(x=self.xcor(),y=new_ycor)
