from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec == 0:
        count_sec="00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        windows.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100,pady=50,bg=YELLOW)

text_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
text_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",font=15,command=start_count)
start_button.grid(row=2,column=0)

start_button = Button(text="Reset",font=15)
start_button.grid(row=2,column=2)

tick_label= Label(text="+",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
tick_label.grid(row=3,column=1)


windows.mainloop()