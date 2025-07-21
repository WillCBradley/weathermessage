Pulls your local forecast (temp in celsius) from a weather API, and sends it to a device of your choice.

**Steps To Set Up**
1. Download "weathermsg.py" from the repo above
2. Sign up to [WeatherAPI.com](https://weatherapi.com). Follow the documentation, and fill in the blanks in the code with your API key in "weather_params"
3. Find your latitude and longitude (I used [LatLong](https://www.latlong.net/)), and add to the "q" key in "weather_params"
4. Sign up for [Pushover](https://pushover.net/), and add your API token and user key to "pushover_params"
5. Add your name to the string on line 130 (in place of "your-name")
6. Run the code locally to ensure all notifications are working as designed
5. Host the code on a free automation platform like [PythonAnywhere](https://www.pythonanywhere.com/), and set to run at your preferred time each day

Note: I believe pushover app has a one-time $5 USD setup fee after a month. I have no affiliation with them whatsoever, but have found it to be useful for my own purposes.
