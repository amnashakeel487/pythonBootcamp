import requests
import smtplib
import datetime as dt
import time

# ==========================
# YOUR INFORMATION
# ==========================

MY_EMAIL = "amnashakeel606@gmail.com"
MY_PASSWORD = "xnfcygpucadrrfoy"

# Your location (Example: Lahore)
MY_LAT = 31.5204
MY_LONG = 74.3587

# ==========================
# CHECK IF ISS IS OVERHEAD
# ==========================

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True

    return False


# ==========================
# CHECK IF IT IS NIGHT
# ==========================

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters,
    )
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.utcnow().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False


# ==========================
# MAIN LOOP
# ==========================

while True:

    time.sleep(60)

    if is_iss_overhead() and is_night():

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(
                user=MY_EMAIL,
                password=MY_PASSWORD,
            )

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky! Go outside and take a look!"
            )