import json
from urllib.request import urlopen


class Location:

    def get_location(self):
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        current_lat_lon = data['loc'].split(",")
        current_lat = (current_lat_lon[0].split("."))[0]
        current_lon = (current_lat_lon[1].split("."))[0]
        return current_lat, current_lon
