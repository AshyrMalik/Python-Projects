from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=-350, y=0)

    def go_up(self):
        new_corr = self.ycor() + 20
        self.goto(self.xcor(), new_corr)

    def go_down(self):
        new_corr = self.ycor() - 20
        self.goto(self.xcor(), new_corr)


