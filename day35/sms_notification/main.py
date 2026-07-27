import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")

LATITUDE = float(os.getenv("LATITUDE"))
LONGITUDE = float(os.getenv("LONGITUDE"))

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

# -------------------------
# Weather API
# -------------------------
URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

# -------------------------
# Check Weather
# -------------------------
will_rain = False

# First 12 forecast entries (~36 hours for 3-hour forecasts)
for forecast in weather_data["list"][:12]:

    weather_id = forecast["weather"][0]["id"]

    if weather_id < 700:
        will_rain = True
        break

# -------------------------
# Send SMS
# -------------------------
if will_rain:

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="☔ Rain is expected today. Don't forget your umbrella!",
        from_=TWILIO_NUMBER,
        to=MY_PHONE_NUMBER,
    )

    print("SMS Sent Successfully!")
    print("Message SID:", message.sid)

else:
    print("No rain expected today.")