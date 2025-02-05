from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=0
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.level+=1
        self.goto(-200,250)
        self.write(f"Level: {self.level} ",align="center",font= FONT)

