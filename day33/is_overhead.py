import requests

# ISS API URL
URL = "http://api.open-notify.org/iss-now.json"

# Send GET request
response = requests.get(url=URL)

# Raise an exception if something went wrong
response.raise_for_status()

# Convert JSON response to Python dictionary
data = response.json()

# Extract latitude and longitude
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Print ISS location
print(f"Latitude : {latitude}")
print(f"Longitude: {longitude}")