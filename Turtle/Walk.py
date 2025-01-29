import turtle as t
import random

def color_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

t.colormode(255)
timm = t.Turtle()
timm.pensize(15)
timm.speed("fastest")

# Directions
directions = [0, 90, 180, 270]

# Random walk loop
for _ in range(300):
    timm.color(color_picker())
    timm.forward(30)
    timm.setheading(random.choice(directions))

# Keep the window open
t.done()
