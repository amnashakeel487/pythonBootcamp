import requests

URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 31.5204
MY_LONG = 74.3587

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print(f"Sunrise Time: {sunrise}")
print(f"Sunset Time : {sunset}")

print(f"\nSunrise Hour: {sunrise_hour}")
print(f"Sunset Hour : {sunset_hour}")