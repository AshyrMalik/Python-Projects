import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)  # Cars should be wider than tall
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))  # Keep cars within visible range

        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move left

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT