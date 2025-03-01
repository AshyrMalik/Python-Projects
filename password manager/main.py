from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    pyperclip.copy(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email= email_entry.get()
    password = password_entry.get()
    if not website or not email or not password:
        messagebox.showinfo(title="Invalid Input", message="Don't leave any field empty")
        return

    is_ok= messagebox.askokcancel(title="website",message=f"These are the entered details: \nEmail: {email} \nPassword : {password}")
    if is_ok:
        with open("data.txt","a") as data_file:
            data_file.write(f"{website} |  {email}| {password}")

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

gen_password = Button(text="Generate", font=("Arial", 10, "bold"), bg="#ffcc00", fg="black", padx=5,command=generate_password)
gen_password.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, font=("Arial", 10, "bold"), bg="#4caf50", fg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)


windows.mainloop()
