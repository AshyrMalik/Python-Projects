from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_result_label.config(text=km)

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
miles_input= Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label= Label(text="0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)

calculate_buttons =Button(text="Calculate",command=miles_to_km)
calculate_buttons.grid(column=1,row=3)


window.mainloop()