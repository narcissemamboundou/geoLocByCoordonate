# -*- coding: utf-8 -*-
"""na.mbd.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BjCKvbAVRkKymzHAukVwI6eihXj9bMqK
"""

# Geocoding library 
!pip install geopy
!pip install folium

import pandas as pd
from geopy.geocoders import Nominatim
import folium
import time

findIT = Nominatim(timeout=10, user_agent = "na.mbd")

#print location by an adress
location = findIT.geocode("port-gentil, gabon").raw
print(location)

def findAdress(latitude, longitude, language="en"):
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return findIT.reverse(coordinates, language=language).raw
    except:
        return findAdress(latitude, longitude)

latitude = -0.7149116
longitude = 8.7797434
address=findAdress(latitude, longitude)
address_geo=address['address']
city=address['address']['city']
print(city)
print(address_geo)
