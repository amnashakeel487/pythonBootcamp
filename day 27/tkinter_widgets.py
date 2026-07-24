from tkinter import *

# ---------------------- FUNCTIONS ---------------------- #

def button_clicked():
    label.config(text=entry.get())

def spinbox_used():
    print(f"Spinbox: {spinbox.get()}")

def scale_used(value):
    print(f"Scale: {value}")

def checkbutton_used():
    print(f"Checkbox: {checked_state.get()}")

def radio_used():
    print(f"Selected Option: {radio_state.get()}")

def listbox_used(event):
    selected = listbox.get(listbox.curselection())
    print(f"Selected Fruit: {selected}")

# ---------------------- WINDOW ---------------------- #

window = Tk()
window.title("Tkinter Widget Examples")
window.minsize(width=500, height=650)
window.config(padx=20, pady=20)

# ---------------------- LABEL ---------------------- #

label = Label(text="This is new text", font=("Arial", 16))
label.pack(pady=5)

# ---------------------- BUTTON ---------------------- #

button = Button(text="Click Me", command=button_clicked)
button.pack(pady=5)

# ---------------------- ENTRY ---------------------- #

entry = Entry(width=35)
entry.insert(0, "Some text to begin with.")
entry.pack(pady=5)

# ---------------------- TEXT ---------------------- #

text = Text(width=30, height=5)
text.insert(END, "Example of multi-line text entry.")
text.pack(pady=5)

# ---------------------- SPINBOX ---------------------- #

spinbox = Spinbox(
    from_=0,
    to=10,
    width=5,
    command=spinbox_used
)
spinbox.pack(pady=5)

# ---------------------- SCALE ---------------------- #

scale = Scale(
    from_=0,
    to=100,
    orient=VERTICAL,
    command=scale_used
)
scale.pack(pady=5)

# ---------------------- CHECKBUTTON ---------------------- #

checked_state = IntVar()

checkbutton = Checkbutton(
    text="Is On?",
    variable=checked_state,
    command=checkbutton_used
)
checkbutton.pack(pady=5)

# ---------------------- RADIO BUTTONS ---------------------- #

radio_state = IntVar()

radio1 = Radiobutton(
    text="Option 1",
    value=1,
    variable=radio_state,
    command=radio_used
)

radio2 = Radiobutton(
    text="Option 2",
    value=2,
    variable=radio_state,
    command=radio_used
)

radio1.pack()
radio2.pack()

# ---------------------- LISTBOX ---------------------- #

listbox = Listbox(height=4)

fruits = ["Apple", "Pear", "Orange", "Banana"]

for fruit in fruits:
    listbox.insert(END, fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack(pady=10)

# ---------------------- MAIN LOOP ---------------------- #

window.mainloop()