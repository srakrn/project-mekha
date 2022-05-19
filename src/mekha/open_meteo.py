import json
import requests

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search?name={name}"
FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"


def location_to_coordinates(location):
    target_api_call = GEOCODING_API_URL.format(name=location)
    response = requests.get(target_api_call)
    response.raise_for_status()
    json_response = json.loads(response.text)
    return (
        json_response["results"][0]["latitude"],
        json_response["results"][0]["longitude"],
    )

def forecast(location, **kwargs):
    additional_suffix = ''
    if len(location) != 2:
        lat, lon = location_to_coordinates(location)
    else:
        lat, lon = location
    if 'hourly' in kwargs:
        additional_suffix += f'&hourly={kwargs["hourly"]}'
    if 'daily' in kwargs:
        additional_suffix += f'&daily={kwargs["daily"]}'
    if 'current_weather' in kwargs:
        additional_suffix += f'&current_weather={kwargs["current_weather"]}'
    target_api_call = FORECAST_API_URL.format(lat=lat, lon=lon)
    target_api_call += additional_suffix
    response = requests.get(target_api_call)
    response.raise_for_status()
    json_response = json.loads(response.text)
    return json_response