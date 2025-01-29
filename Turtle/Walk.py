import turtle as t
import random

timm= t.Turtle()



colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [90,180,270,0]
for _ in range(300):
    timm.color(random.choice(colors))
    timm.forward(30)
    timm.setheading(random.choice(direction))

