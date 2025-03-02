from cProfile import label
from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv(r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\data\french_words.csv")
to_learn = df.to_dict(orient="records")


def next_card():
    word = random.choice(to_learn)
    canvas.itemconfig(label1,text="French")
    canvas.itemconfig(label2,text=word["French"])


windows = Tk()
windows.title("Flash Card App")
windows.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
foreground = PhotoImage(file=r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\images\card_front.png")
canvas.create_image(400, 263,image=foreground)

label1 = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
label2 = canvas.create_text(400, 263, text="Label 2", font=("Arial", 60, "bold"), fill="black")


canvas.grid(row=0 ,column=0, columnspan=3)

#Buttons

right_image = PhotoImage(file=r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\images\right.png")
right_button = Button(image=right_image, highlightthickness=0,pady=50 ,command=next_card)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file=r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,pady=50,command=next_card)
wrong_button.grid(row=1, column=2)

next_card()

windows.mainloop()

