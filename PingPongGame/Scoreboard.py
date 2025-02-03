from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"Player 1 Score: {self.l_score} ",align="center",font= ("Courier",20,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font= ("Courier",60,"normal"))

    def update_rscore(self):
        self.r_score+=1


    def update_lscore(self):
        self.l_score+=1