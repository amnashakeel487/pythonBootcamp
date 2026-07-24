from tkinter import *

# ---------------------- FUNCTION ---------------------- #

def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609, 2)
    km_result.config(text=kilometers)

# ---------------------- WINDOW ---------------------- #

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=180)
window.config(padx=20, pady=20)

# ---------------------- ENTRY ---------------------- #

miles_input = Entry(width=10)
miles_input.insert(END, "0")
miles_input.grid(row=0, column=1)

# ---------------------- LABELS ---------------------- #

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# ---------------------- BUTTON ---------------------- #

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

# ---------------------- MAIN LOOP ---------------------- #

window.mainloop()