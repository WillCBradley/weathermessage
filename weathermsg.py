import requests
import json
from datetime import datetime

# Variables for setup

weather_key = "add weatherAPI key here"
your_lat = "add latitude here"
your_lon = "add longitude here"
pushover_token = "add pushover token here"
pushover_user = "add pushover user here"
your_first_name = "add your first name here"

# Remainder of code below doesn't need to be touched for setup

weather_url = "http://api.weatherapi.com/v1/forecast.json"
weather_params = {
    'key': weather_key,
    'q': f"{your_lat},{your_lon}"
}

response = requests.get(weather_url, params=weather_params)
data = response.json()
# print(json.dumps(data, indent=2))

# Get Today's Date (YYYY-MM-DD)
date = datetime.today().strftime('%Y-%m-%d')

# Today's Hours Array
hours = []

# Narrow Down To Today's Hours
for object in data["forecast"]["forecastday"][0]["hour"]:
        hours.append(object)

# Find Max Temp + Hour
max_temp = -1000
for object in hours:
    if object["temp_c"] > max_temp:
        max_temp = object["temp_c"]
        max_temp_time_raw = int(object["time"][11:13])

if max_temp_time_raw > 12:
    max_temp_time = str(max_temp_time_raw - 12) + "pm"
elif max_temp_time_raw == 12:
    max_temp_time = "12pm"
else:
    max_temp_time = str(max_temp_time_raw) + "am"

# Control For Higher Temp In Hour vs Overall Max
highest_temp = max_temp if max_temp > data["forecast"]["forecastday"][0]["day"]["maxtemp_c"] else data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]

# Output Max Temp + Corresponding Hour
temp_string = f"Max temp is {highest_temp} (expected around {max_temp_time})."
# print(temp_string)

# Output Basic Rain Data (Everything Else Can Just Be Done W/ Radar)
rain_string = f"{data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]}% chance of rain, with {data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]}mm expected."
# print(rain_string)

# All Together
output = f"Good morning, {your_first_name}. {temp_string} {rain_string}"
print(output)


# Output To Iphone

pushover_params = {
    "token": f"{pushover_token}",
    "user": f"{pushover_user}",
    "message": output
}

post_output = requests.post("https://api.pushover.net/1/messages.json", params=pushover_params)