# coding: utf-8
''' Version 1  '''
import sys
import interpreter.record
import interpreter.sensor
import services.geocoding
import services.route
import services.costs
import services.maps

mode= "fastest;truck"
trailers_count= "1"

def get(audio_data):
	file_route = interpreter.record.file(audio_data)
	origin, destination = interpreter.sensor.extract_route_from_audio(file_route)
	waypoint0, waypoint1 = services.geocoding.get_route_coords(origin, destination)
	print(waypoint0, waypoint1)
	route_response =services.route.get(waypoint0, waypoint1, mode, trailers_count)
	route_costed = services.costs.add(route_response)
	route_maps = services.maps.images(route_costed)
	route_detailed = route_points(route_maps, origin, destination)
	return route_costed

def route_points(route, origin, destination):
	route["response"]["points"] = {
		"origin": str(origin).title(),
		"destination": str(destination).title()
	}
	return route