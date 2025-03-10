from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer =NONE
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    text_label.config(text="Timer",fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    short_break =SHORT_BREAK_MIN*60
    big_break= LONG_BREAK_MIN*60
    work_time =WORK_MIN*60

    reps +=1
    if reps == 8:
        print("wwe")
        count_down(big_break)
        text_label.config(text="Break",fg=PINK,bg=YELLOW,font=(FONT_NAME,50,"bold"))

    elif reps %2 == 0:
        print("raw")
        count_down(short_break)
        text_label.config(text="Break",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))


    else:
        print(work_time)
        print(big_break)
        print("smack")
        text_label.config(text="WORK",fg=RED,bg=YELLOW,font=(FONT_NAME,50,"bold"))
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1)

    else:
        mark =""
        for _ in range(math.floor(reps/2)):
            mark+="+"

        tick_label.config(text=mark)
        start_count()

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

reset_button = Button(text="Reset",font=15,command=reset_timer)
reset_button.grid(row=2,column=2)

tick_label= Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
tick_label.grid(row=3,column=1)


windows.mainloop()