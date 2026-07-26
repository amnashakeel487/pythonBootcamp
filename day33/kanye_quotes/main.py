from tkinter import *
import requests

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- API ------------------------------- #
def get_quote():
    try:
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()

        data = response.json()
        quote = data["quote"]

        canvas.itemconfig(quote_text, text=quote)

    except requests.exceptions.RequestException:
        canvas.itemconfig(
            quote_text,
            text="Could not fetch quote.\nCheck your internet connection."
        )


# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=414, bg=BACKGROUND_COLOR, highlightthickness=0)

quote_bg = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=quote_bg)

quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white",
)

canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")

kanye_button = Button(
    image=kanye_img,
    highlightthickness=0,
    borderwidth=0,
    command=get_quote
)

kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()