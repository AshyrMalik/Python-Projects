BACKGROUND_COLOR = "#B1DDC6"


windows = Tk()
windows.title("Flash Card App")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Buttons

right_image = PhotoImage(file=r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\images\right.png")
right_button = Button(image=right_image, highlightthickness=0,padx=50,pady=50 )
right_button.grid(row=2, column=1)

wrong_image = PhotoImage(file=r"C:\Users\HP\PycharmProjects\Python-Projects\FlashCard App for Language Leanrning\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=2, column=6)



windows.mainloop()

