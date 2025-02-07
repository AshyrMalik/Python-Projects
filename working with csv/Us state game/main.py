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

        # Get the row for the guessed state
        guessed_state = data[data["state"].str.lower() == user_guess]

        # Move turtle to the guessed state's position
        tim.goto(int(guessed_state["x"].iloc[0]), int(guessed_state["y"].iloc[0]))
        tim.write(f"{user_guess.title()}", align="center", font=("Courier", 10, "normal"))

        count = 0  # Reset count when a correct answer is given

    if count == 1:
        is_on = False
turtle.mainloop()
pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


