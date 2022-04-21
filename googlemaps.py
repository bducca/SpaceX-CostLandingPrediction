Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import googlemaps
import requests
import json
from __future__ import print_function
import folium

class ADGGoogleMaps:
    def __init__(self, google_api_secret, address):
        self.google_api_secret = google_api_secret
        self.address = address
        self.gmaps = googlemaps.Client(key=self.google_api_secret)
        self.geocode_result = gmaps.geocode(self.address)
        self.json_format = json.dumps(geocode_result)
        self.results = []

    def GetCordsFromAddress(self):
        cords = find_values('location', self.json_format)
        locationdict = cords[0]
        cords = list(locationdict.values())
        return cords

    def findvalues(self, id, json_repr):
        results = []

        def _decode_dict(self, a_dict):
            try:
                results.append(a_dict[id])
            except KeyError:
                pass
            return a_dict
        json.loads(json_repr, object_hook=_decode_dict)
        return results

    def ReturnMap(self,size):
        mapit = folium.Map( location=self.GetCordsFromAddress,zoom_start = size)
        return mapit