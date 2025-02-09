import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"w")

game_is_on = True
count= 6
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count==6:
        car_manager.create_car()
        count=1
    for car in car_manager.all_cars:
        if car.distance(player) <30:
            game_is_on= False

    if player.ycor()>300:
        player.reset()
        car_manager.level_up()
        scoreboard.update_scoreboard()

    count+=1
    car_manager.move()



screen.exitonclick()