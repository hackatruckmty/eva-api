import requests
import os

key_map = os.environ['GMAPS_API_KEY']
geo_url = "https://maps.googleapis.com/maps/api/geocode/json"

def get_route_coords(originCity,destinationCity):
    originLatlon = geocode(originCity)
    destinationLatlon = geocode(destinationCity)
    return originLatlon, destinationLatlon

def geocode(city):
    print(city)
    params_geo = {
        "address": city+ ", México",
        "key":key_map,
        #"components":"country:MX"
    }
    r = requests.get(geo_url, params=params_geo).json()
    coords = r["results"][0]["geometry"]["location"]
    return str(coords["lat"]) + "," + str(coords["lng"])