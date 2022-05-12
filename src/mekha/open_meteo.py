import json
import requests

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search?name={name}"


def location_to_coordinates(location):
    target_api_call = GEOCODING_API_URL.format(name=location)
    response = requests.get(target_api_call)
    response.raise_for_status()
    json_response = json.loads(response.text)
    return (
        json_response["results"][0]["latitude"],
        json_response["results"][0]["longitude"],
    )
