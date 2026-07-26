import smtplib
import datetime as dt
import random

# ---------------------------- EMAIL DETAILS ---------------------------- #

MY_EMAIL = "amnashakeel606@gmail.com"
APP_PASSWORD = "your_password"

# ---------------------------- CHECK DAY ---------------------------- #

now = dt.datetime.now()

# Monday = 0
if now.weekday() == 6:

    # Read all quotes
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    # Choose a random quote
    random_quote = random.choice(quotes)

    # Send Email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(
            user=MY_EMAIL,
            password=APP_PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Sunday Motivation\n\n{random_quote}"
        )

    print("Motivational email sent successfully!")

else:
    print("Today is not Sunday.")