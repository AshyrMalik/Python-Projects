import turtle as t
import random

t.colormode(255)
timm = t.Turtle()
timm.speed("fastest")

def color_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for i in range(200):
        timm.color(color_picker())
        timm.circle(100)
        timm.setheading(timm.heading()+ size_of_gap)



draw_spirograph(5)