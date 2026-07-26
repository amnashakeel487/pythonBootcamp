import pandas as pd
import datetime as dt
import random
import smtplib

# ---------------- EMAIL DETAILS ---------------- #

MY_EMAIL = "amnashakeel606@gmail.com"
APP_PASSWORD = "your_password"

# ---------------- TODAY ---------------- #

today = dt.datetime.now()

today_tuple = (today.month, today.day)

# ---------------- READ CSV ---------------- #

data = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (row.month, row.day): row
    for (index, row) in data.iterrows()
}

# ---------------- CHECK BIRTHDAY ---------------- #

if today_tuple in birthdays_dict:

    birthday_person = birthdays_dict[today_tuple]

    random_letter = random.randint(1, 3)

    with open(f"letter_templates/letter_{random_letter}.txt") as file:
        letter = file.read()

    letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(
            user=MY_EMAIL,
            password=APP_PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )

    print("Birthday email sent!")

else:
    print("No birthdays today.")