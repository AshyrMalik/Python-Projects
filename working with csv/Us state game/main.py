import turtle
from turtle import Screen , Turtle
import pandas as pd


screen = Screen()
screen.title("U.S. State game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


