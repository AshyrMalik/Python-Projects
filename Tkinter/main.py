import tkinter

# window = tkinter.Tk()
# window.title("My first Gui")
# window.minsize(width=500, height= 300)
#
# my_label = tkinter.Label(text="Hello world")
# my_label.pack(side ="left")
#

def add(*args):
    sum = 0
    for num in args:
        sum+=num

    return sum

print(add(5,5,5,5,5))

#
# window.mainloop()