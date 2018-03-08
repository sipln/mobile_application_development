# Author Sipln
# The test program to my "Greate_Circle_Dist.py" file 

import requests

def main():

	latA, longA = map(float, input("Latitude A, Longitude A: ").split())
	latB, longB = map(float, input("Latitude B, Longitude B: ").split())

	base = "http://localhost:5000/GetDistance?"
	params = "latA={lat_A}&longA={long_A}&latB={lat_B}&longB={long_B}".format(
		lat_A=latA,
		long_A=longA,
		lat_B=latB,
		long_B=longB
	)

	url = "{base}{params}".format(base=base, params=params)
	response = requests.get(url)
	response = response.json()

	print(response['distance'])


if __name__ == "__main__":
	main()


# Test with the two given A, B point
# Latitude, Longitude of A: 21.028511  105.804817 ( Hanoi )
# Latitude, Longitude of B: 10.762622  106.660172 (Ho Chi Minh)
# 21.028511  105.804817 10.762622  106.660172
