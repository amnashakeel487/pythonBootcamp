from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")


def generate_password():
    password_entry.delete(0, END)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please don't leave Website or Password empty!"
        )

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\n\n"
                    f"Website: {website}\n"
                    f"Email: {email}\n"
                    f"Password: {password}\n\n"
                    f"Save?"
        )

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"{website} | {email} | {password}\n"
                )

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- Labels ------------------------------- #

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5, sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5, sticky="e")

# ---------------------------- Entries ------------------------------- #

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="we", padx=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=5)
email_entry.insert(0, "your_email@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="we", padx=5)

# ---------------------------- Buttons ------------------------------- #

generate_button = Button(
    text="Generate Password",
    width=16,
    command=generate_password
)
generate_button.grid(row=3, column=2, padx=5)

add_button = Button(
    text="Add",
    command=save
)
add_button.grid(row=4, column=1, columnspan=2, sticky="we", pady=10)
window.mainloop()