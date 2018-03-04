import math

latA, longA = map(float, input("Latitude, Longitude of A: ").split())
latB, longB = map(float, input("Latitude, Longitude of B: ").split())

A_Coord = [latA, longA]
B_Coord = [latB, longB]

# Use the Harversine formula to calculate the great-circle distance between two point
# 		Haversine formula:
# 			a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
# 			c = 2 ⋅ atan2( √a, √(1−a) )
# 			d = R ⋅ c
#
# 			where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
# 			note that angles need to be in radians to pass to trig functions!

def CalcDistance(A_Coord, B_Coord):

	R = 6371 # Count in Km

	a = math.pow(math.sin((math.radians(A_Coord[0]) - math.radians(B_Coord[0]))/2),2) + \
		math.cos(math.radians(A_Coord[0]))*math.cos(math.radians(B_Coord[0]))*math.pow(math.sin((math.radians(A_Coord[1])-math.radians(B_Coord[1]))/2),2)

	c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

	d = R*c

	return d

print("Distance between A and B is ", CalcDistance(A_Coord, B_Coord), " Km")

# Test with the two given A, B point
# Latitude, Longitude of A: 21.028511  105.804817 ( Hanoi )
# Latitude, Longitude of B: 10.762622  106.660172 (Ho Chi Minh)
