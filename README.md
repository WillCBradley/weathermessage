Pulls your local forecast (temp in celcius) from a weather API, and sends it to a device of your choice.

**Steps To Install**
1. Sign up to [WeatherAPI.com](https://weatherapi.com). Follow the documentation, and fill in the blanks in the code with your API key
2. Find your latitude and longitude (I used [LatLong](https://www.latlong.net/)), and add to the "q" key in "weather_params"
3. Sign up for [Pushover](https://pushover.net/), and add your API token and user key to "pushover_params"
4. Run the code locally to ensure all notifications are working as designed
5. Host the code on a free automation platform like [PythonAnywhere](https://www.pythonanywhere.com/), and set to run at a set time each day

Note: I believe pushover app has a one-time $5 USD setup fee after a month. I have no affiliation with them whatsoever, but have found it to be useful for my own purposes.
