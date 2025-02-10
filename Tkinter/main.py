from tkinter import *

window = Tk()
window.title("My first Gui")
window.minsize(width=500, height= 300)

my_label = Label(text="heyyyyyyy")
my_label.pack()

# def add(*args):
#     sum = 0
#     for num in args:
#         sum+=num
#
#     return sum
#
# print(add(5,5,5,5,5))
input = Entry()
input.pack()

def button_click():
    my_label.config(text=input.get())


button = Button(text="Wwer",command=button_click)
button.pack()





window.mainloop()