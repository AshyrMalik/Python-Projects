from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt","a") as data_file:

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50, bg="#f7f5dd")

canvas = Canvas(width=200, height=200, bg="#f7f5dd", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12, "bold"), bg="#f7f5dd")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email:", font=("Arial", 12, "bold"), bg="#f7f5dd")
email_label.grid(row=2, column=0, sticky="e")

pass_label = Label(text="Password:", font=("Arial", 12, "bold"), bg="#f7f5dd")
pass_label.grid(row=3, column=0, sticky="e")

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = Entry(width=33)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "asharmalik6231@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

gen_password = Button(text="Generate", font=("Arial", 10, "bold"), bg="#ffcc00", fg="black", padx=5)
gen_password.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, font=("Arial", 10, "bold"), bg="#4caf50", fg="white")
add_button.grid(row=4, column=1, columnspan=2, pady=5)


windows.mainloop()
