from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20,pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file= "logo.png")
canvas.create_image(100,100,image=logo)
canvas.pack()



windows.mainloop()
