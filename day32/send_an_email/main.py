import smtplib

# ---------------------------- YOUR DETAILS ------------------------------- #

MY_EMAIL = "amnashakeel606@gmail.com"
APP_PASSWORD = "your_password"

RECEIVER_EMAIL = "amnashakeel2101@gmail.com"

# ---------------------------- SEND EMAIL -------------------------------- #

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # Secure the connection
    connection.starttls()

    # Login
    connection.login(
        user=MY_EMAIL,
        password=APP_PASSWORD
    )

    # Send Email
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEIVER_EMAIL,
        msg=(
            "Subject:Hello from Python!\n\n"
            "Congratulations!\n\n"
            "This email was sent using Python and the SMTP library.\n\n"
            "Happy Coding!\n"
            "- Amna"
        )
    )

print("Email sent successfully!")