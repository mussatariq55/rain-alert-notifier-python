import requests
from smtplib import SMTP
import os

# ----------------------- USER CONFIGURATION ----------------------- #

# Store sensitive information like email and API keys in environment variables for security
MY_EMAIL = os.getenv("RAIN_ALERT_EMAIL")          # e.g., youremail@gmail.com
MY_PASSWORD = os.getenv("RAIN_ALERT_APP_PASSWORD") # App password (never use real email password)
API_KEY = os.getenv("OPENWEATHER_API_KEY")         # Get from https://openweathermap.org/api

# ------------------------ API SETUP ------------------------ #

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Coordinates and forecast count
parameters = {
    "lat": 35.09,          # Your Latitude
    "lon": 77.15,          # Your Longitude
    "appid": API_KEY,      # Secure API key
    "cnt": 4               # Number of time intervals (3-hour intervals)
}

# ---------------------- GET WEATHER DATA ---------------------- #

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(f"Status Code: {response.status_code}")  # Optional: Log request status

# ---------------------- CHECK FOR RAIN ---------------------- #

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Weather codes below 700 usually mean rain
        will_rain = True

# ---------------------- SEND EMAIL ALERT ---------------------- #

if will_rain:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Weather Alert!\n\nBring your umbrella, it's going to rain today ☔"
        )
