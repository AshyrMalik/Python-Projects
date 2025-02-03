from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmov=10
        self.ymov = 10

    def move(self):
        x_corr=self.xcor()+self.xmov
        y_corr=self.ycor()+self.ymov
        self.goto(x_corr,y_corr)

    def bounce_y(self):
        self.ymov= self.ymov * -1

    def bounce_x(self):
        self.xmov=self.xmov* -1
    def reset(self):
        self.goto(0,0)