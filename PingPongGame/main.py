from turtle import Turtle,Screen


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Ping Pong")
screen.tracer(0)

paddle1 = Turtle()
paddle1.color("white")
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(x=-350,y=0)

paddle2 = Turtle()
paddle2.color("white")
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(x=350,y=0)

def go_up():
    new_corr=paddle1.ycor()+20
    paddle1.goto(paddle1.xcor(),new_corr)

def go_down():
    new_corr=paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_corr)

screen.listen()
screen.onkey(key="w",fun=go_up)
screen.onkey(key="s",fun=go_down)
is_on = True
while is_on:
    screen.update()



screen.exitonclick()