from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")


def generate_password():
    password_entry.delete(0, END)

    password_letters = [
        random.choice(letters)
        for _ in range(random.randint(8, 10))
    ]

    password_symbols = [
        random.choice(symbols)
        for _ in range(random.randint(2, 4))
    ]

    password_numbers = [
        random.choice(numbers)
        for _ in range(random.randint(2, 4))
    ]

    password_list = (
        password_letters +
        password_symbols +
        password_numbers
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    # Copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please don't leave any fields empty!"
        )

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\n\n"
                    f"Website: {website}\n"
                    f"Email: {email}\n"
                    f"Password: {password}\n\n"
                    f"Is it okay to save?"
        )

        if is_ok:

            try:
                # Read existing data
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                # Create new file if it doesn't exist
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Update existing data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                # Clear input fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- SEARCH ------------------------------- #

def search():

    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No Data File Found."
        )

    else:
        if website in data:

            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )

        else:
            messagebox.showinfo(
                title="Not Found",
                message=f"No details for '{website}' exist."
            )

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
# ---------------- Canvas ---------------- #

canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

# ---------------- Labels ---------------- #

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)


# ---------------- Entries ---------------- #

website_entry = Entry(width=24)
website_entry.grid(row=1, column=1, padx=5)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2, padx=5)
email_entry.insert(0, "your_email@example.com")

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, padx=5)


# ---------------- Buttons ---------------- #

search_button = Button(
    text="Search",
    width=14,
    command=search
)
search_button.grid(row=1, column=2)

generate_button = Button(
    text="Generate Password",
    width=14,
    command=generate_password
)
generate_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=36,
    command=save
)
add_button.grid(row=4, column=1, columnspan=2, pady=8)

window.mainloop()