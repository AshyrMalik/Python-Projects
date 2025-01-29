import turtle as t
import random
timm= t.Turtle()

def draw_shapes(num_of_shapes,color):

    angle = 360 / num_of_shapes
    timm.color(color)
    for i in range(num_of_shapes):
        timm.forward(100)
        timm.right(angle)


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for shapes in range(3,11):
    color = random.choice(colors)
    draw_shapes(shapes,color)
