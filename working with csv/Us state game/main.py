import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load data
data = pd.read_csv("50_states.csv")

# Convert states column to a lowercase list
list_of_states = data["state"].str.lower().tolist()

# Game loop
is_on = True
guessed_list=[]
while is_on:

    user_guess = screen.textinput(title=f"{(len(guessed_list))}/50 correct states", prompt="Enter another state name that you know").lower()

    if user_guess in list_of_states:
        guessed_list.append(user_guess)
        tim = Turtle()
        tim.penup()
        tim.hideturtle()

        # Get the row for the guessed state
        guessed_state = data[data["state"].str.lower() == user_guess]

        # Move turtle to the guessed state's position
        tim.goto(int(guessed_state["x"].iloc[0]), int(guessed_state["y"].iloc[0]))
        tim.write(f"{user_guess.title()}", align="center", font=("Courier", 10, "normal"))

        continue

    is_on = False


turtle.mainloop()
