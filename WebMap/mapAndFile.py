#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:59:00 2020

@author: jovillal

Builds a map with folium and loads coordinates of volcanos form a text file
It also puts a volcano name that points to a google search
"""

import folium
import pandas #use this to read a csv file

data = pandas.read_csv("Volcanoes.txt")
lon = list(data['LON']) #get the longitude information
lat = list(data['LAT']) #get the latitude information
elev = list(data["ELEV"]) #get the elevation information
name = list(data["NAME"]) #get the name of the volcanoes

#Build some html code
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#This creates a map object, the location is in latitude and longitude, think of this as a layer
#map = folium.Map(location=[38.58,-99.09], zoom_start = 9, tiles = "Stamen Terrain")

#Now add features, use zip to iterate over several lists
#fg = folium.FeatureGroup(name='My map')

#for lt, ln in zip(lat,lon):
#    fg.add_child(folium.Marker(location=[lt,ln], popup="A volcano",icon = folium.Icon(color = 'orange')))

#map.add_child(fg)

#This saves the map to an html format
#map.save("Map4.html")

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("Map_html_popup_advanced.html")