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

data = pd.read_csv("50_states.csv")
states = data["states"]
list_of_states =states.list().lower()

is_on = True

while is_on:
    user_guess = screen.textinput(title="Name a state", prompt="Enter another state name that you know  ")

    if user_guess in list_of_states:
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        guessed_state= data[data["state"].lower()==user_guess]
        tim.goto(guessed_state.x,guessed_state.y)
        tim.write(f"{user_guess}", align="center", font=("Courier", 7, "normal"))
        count=0

    if count == 1:
        is_on = False
turtle.mainloop()
pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


