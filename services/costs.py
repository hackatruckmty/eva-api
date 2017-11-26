
def add(route):
	kms = route["response"]["route"][0]["leg"][-1]["length"]/1000.0
	# This weights are hardcoded
	costs = {
		"km": kms, 
		"fuel": kms*4.0, 
		"salary": kms*0.2901+5592.3, 
		"expenses": kms*0.7254+280.53,
	}
	route["response"]["costs"] = costs
	return route