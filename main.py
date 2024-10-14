from tkinter import *


def button_clicked():
    miles = int(miles_input.get())
    km = round(1.6 * miles,2)

    converted_label.config(text=str(km))


window = Tk()
window.title("Miles to kilometers convertor")
window.config(padx=20, pady=20)

# Label
miles_label = Label(text="Miles", font=("Times New Roman", 14))
text_label = Label(text="is equal to", font=("Times New Roman", 14))
converted_label = Label(text="0", font=("Times New Roman", 14))
km_label = Label(text="km", font=("Times New Roman", 14))

miles_label.grid(column=2, row=0)
text_label.grid(column=0, row=1)
converted_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate",font=("Times New Roman", 14), command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

# Entry
miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)



window.mainloop()