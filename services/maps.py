import os

map_url = "https://image.maps.cit.api.here.com/mia/1.6/routing"
app_id = os.environ["ROUTE_APP_ID"]
app_code = os.environ["ROUTE_APP_CODE"]


def images(route):
	path = route["response"]["path"]
	route["response"]["maps"] = {
		"tall": generate_map_url(path, 400, 600),
		"wide": generate_map_url(path, 600, 400)
	}

	return route


def generate_map_url(path, width, height):
	params = {
		"app_id":app_id,
		"app_code": app_code,
		"lc":"1652B4",
		"lw":6,
		"t":0,
		"ppi":320,
		"w": width,
		"h": height
	}

	for i,point in enumerate(path):
		params["waypoint"+str(i)] =str(point["latitude"])+","+ str(point["longitude"])

	url_output = map_url

	for i, param in enumerate(params):
		if i == 0:
			url_output = url_output + "?"
		else:
			url_output = url_output + "&"
		url_output = url_output+ param + "=" + str(params[param])
	return url_output