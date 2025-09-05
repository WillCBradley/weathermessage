Pulls your local forecast (temp in celsius) from a weather API, and sends it to a device of your choice.

_(Somebody has probably built a better version, but if you want to use this one, instructions are below.)_

**Steps To Set Up**
1. Download "weathermsg.py" from the repo above
2. Sign up to [WeatherAPI.com](https://weatherapi.com). Follow the documentation, and assign your API key to weather_key
3. Find your latitude and longitude (I used [LatLong](https://www.latlong.net/)), and assign to your_lat and your_lon
4. Sign up for [Pushover](https://pushover.net/), and assign your API token and user key to pushover_token and pushover_key respectively
5. Assign your first name to your_first_name variable
6. Run the code locally to ensure all notifications are working as designed
5. Host the code on a free automation platform like [PythonAnywhere](https://www.pythonanywhere.com/), and set to run at your preferred time each day

Note: pushover app has a one-time $5 USD setup fee after a month. I have no affiliation with them whatsoever, but have paid for it, and found it to be useful for my own purposes.
