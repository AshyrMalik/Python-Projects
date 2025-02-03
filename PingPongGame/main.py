import time
from turtle import Turtle,Screen
from PingPongGame.Scoreboard import ScoreBoard
from PingPongGame.ball import Ball
from PingPongGame.paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Ping Pong")
screen.tracer(0)

paddle1= Paddle(-350)
paddle2= Paddle(350)
score=ScoreBoard()

ball= Ball()
screen.listen()
screen.onkey(key="w",fun=paddle1.go_up)
screen.onkey(key="s",fun=paddle1.go_down)
screen.onkey(key="Up",fun=paddle2.go_up)
screen.onkey(key="Down",fun=paddle2.go_down)
is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(paddle2) < 50) or (ball.xcor() < -320 and ball.distance(paddle1) < 50):
        ball.bounce_x()

    if ball.xcor()<-380:
        score.update_lscore()
        score.update_score()
        ball.reset()
    if ball.xcor()>380:
        score.update_rscore()
        score.update_score()
        ball.reset()

screen.exitonclick()