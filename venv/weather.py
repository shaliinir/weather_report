import requests # library for calling APIs
url = "https://api.open-meteo.com/v1/forecast" # API address (free, no key needed)
params = {
"latitude": 13.08, # Chennai
"longitude": 80.27,
"current": "temperature_2m,wind_speed_10m", # values we want back
}
try:
    response = requests.get(url, params=params, timeout=10) 
    response.raise_for_status() # turn 4xx/5xx codes into an error
    data = response.json() # JSON text -> Python dict
    temp = data["current"]["temperature_2m"] # dig into the dict
    print(f"Chennai: {temp}°C")
except requests.exceptions.RequestException as e: # network or API problem
    print(f"Could not get weather: {e}")
