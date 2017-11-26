import requests
import os

app_id = os.environ["ROUTE_APP_ID"]
app_code = os.environ["ROUTE_APP_CODE"]
url = "https://route.cit.api.here.com/routing/7.2/calculateroute.json"

def get(waypoint0, waypoint1, mode, trailers_count):
    
    params = {
    "waypoint0":waypoint0,
    "waypoint1":waypoint1,
    "mode": mode,
    "trailersCount": trailers_count,
    "app_id": app_id,
    "app_code": app_code,
    }
    r = requests.get(url, params=params)
    route = enrich_route(r.json())
    return route


def enrich_route(route):
    maneuvers = route["response"]["route"][0]["leg"][0]["maneuver"]
    route["response"]["path"] = [maneuver["position"] for maneuver in maneuvers]
    return route