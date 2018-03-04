import requests

# This function is used for converting  a given geographic coordinate to a address respectively.


def RevGeo():


    # latitude = 10.817996728 106.651164062
    # longitude = 106.651164062

    latitude, longitude = map(float, input("Latitude, Longitude: ").split());

    sensor = 'false'

    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )

    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    response = response.json()

    print (response['results'][0]['formatted_address'])
    # print(latitude, longitude)

RevGeo()
