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
canvas.grid(row=0,column=1)

# Labels Column
website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email")
email_label.grid(row=2,column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3,column=0)






windows.mainloop()
