import requests
import json
from datetime import datetime

weather_key = "your-key"
weather_url = "http://api.weatherapi.com/v1/forecast.json"
weather_params = {
    'key': weather_key,
    'q': "your-lat,your-lon"
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

# # Arrays For UV Cutoffs
uv_above_3 = []
uv_above_5 = []
uv_above_8 = []

# Filter To Find All Times When UV Is Above 3, 5, and 8. Store In Corresponding Array.
for object in hours:
    if object["uv"] > 3:
        uv_above_3_raw = int(object["time"][11:13])
        if uv_above_3_raw >= 12:
            uv_above_3_time = str(uv_above_3_raw - 12) + "pm"
        else:
            uv_above_3_time = str(uv_above_3_raw) + "am"
        uv_above_3.append(uv_above_3_time)

for object in hours:
    if object["uv"] > 5:
        uv_above_5_raw = int(object["time"][11:13])
        if uv_above_5_raw >= 12:
            uv_above_5_time = str(uv_above_5_raw - 12) + "pm"
        else:
            uv_above_5_time = str(uv_above_5_raw) + "am"
        uv_above_5.append(uv_above_5_time)

for object in hours:
    if object["uv"] > 8:
        uv_above_8_raw = int(object["time"][11:13])
        if uv_above_8_raw >= 12:
            uv_above_8_time = str(uv_above_8_raw - 12) + "pm"
        else:
            uv_above_8_time = str(uv_above_8_raw) + "am"
        uv_above_8.append(uv_above_8_time)


# Find Time 1hr After First And Last Item In Each Array (Since These Are The Only We Could Need To Access)
if uv_above_3:
    time_after_start_3 = str((int(uv_above_3[0][0:2])+1)) + uv_above_3[0][2:]
    if len(uv_above_3) > 1:
        time_after_end_3 = str((int(uv_above_3[-1][0:2])+1)) + uv_above_3[-1][2:]

if uv_above_5:
    time_after_start_5 = str((int(uv_above_5[0][0:2])+1)) + uv_above_5[0][2:]
    if len(uv_above_5) > 1:
        time_after_end_5 = str((int(uv_above_5[-1][0:2])+1)) + uv_above_5[-1][2:]

if uv_above_8:
    time_after_start_8 = str((int(uv_above_8[0][0:2])+1)) + uv_above_8[0][2:]
    if len(uv_above_8) > 1:
        time_after_end_8 = str((int(uv_above_8[-1][0:2])+1)) + uv_above_8[-1][2:]

# Assign String To Each UV Cutoff, Removing Redundant Ones
if uv_above_3:
    if len(uv_above_3) == 1:
        time_above_3 = f"The UV will exceed 3 between {uv_above_3[0]} and {time_after_start_3}"
    else:
        time_above_3 = f"The UV will exceed 3 between {uv_above_3[0]} and {time_after_end_3}"
    if uv_above_5:
        if len(uv_above_5) == 1:
            time_above_5 = f", will exceed 5 between {uv_above_5[0]} and {time_after_start_5}"
        else:
            time_above_5 = f", will exceed 5 between {uv_above_5[0]} and {time_after_end_5}"
        if uv_above_8:
            if len(uv_above_8) == 1:
                time_above_8 = f", and will exceed 8 between {uv_above_8[0]} and {time_after_start_8}"
            else:
                time_above_8 = f", will exceed 8 between {uv_above_8[0]} and {time_after_end_8}"  
        else: time_above_8 = ", and won't exceed 8."
    else:
        time_above_5 = ", and won't exceed 5."
        time_above_8=""
else:
    time_above_3 = "The UV will not exceed 3 today."
    time_above_5 = ""
    time_above_8 = ""

# Output UV Findings
uv_string = f"{time_above_3}{time_above_5}{time_above_8}"

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
output = f"Good morning, your-name. {temp_string} {rain_string} {uv_string}"
print(output)


# Output To Iphone

pushover_params = {
    "token": "your-token",
    "user": "your-user",
    "message": output
}

post_output = requests.post("https://api.pushover.net/1/messages.json", params=pushover_params)