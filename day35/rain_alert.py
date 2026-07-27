import requests

# -----------------------------
# Your OpenWeather API Key
# -----------------------------
API_KEY = "1475833d0b78b6fefa0fb8b730ac22f9"

# -----------------------------
# Your Location
# Replace with your own latitude
# and longitude
# -----------------------------
LATITUDE = 31.204282022494823    # Lahore
LONGITUDE = 73.94024616606596

# -----------------------------
# API Parameters
# -----------------------------
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# -----------------------------
# API Request
# -----------------------------
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()

weather_data = response.json()

# -----------------------------
# Check Next 12 Forecast Entries
# -----------------------------
will_rain = False

for forecast in weather_data["list"][:12]:
    weather_id = forecast["weather"][0]["id"]

    if weather_id < 700:
        will_rain = True

# -----------------------------
# Output
# -----------------------------
if will_rain:
    print("☔ Bring an umbrella today!")
else:
    print("🌞 No rain expected.")