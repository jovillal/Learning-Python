#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:58:14 2020

@author: jovillal
Add color to a map marker based on another atribute
Also, use circles as markers
"""

import folium
import pandas #use this to read a csv file

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

data = pandas.read_csv("Volcanoes.txt")
lon = list(data['LON']) #get the longitude information
lat = list(data['LAT']) #get the latitude information
elev = list(data["ELEV"]) #get the elevation information
name = list(data["NAME"]) #get the name of the volcanoes

#This creates a map object, the location is in latitude and longitude, think of this as a layer
map = folium.Map(location=[38.58,-99.09], zoom_start = 9, tiles = "Stamen Terrain")

#Now add features, use zip to iterate over several lists
fg = folium.FeatureGroup(name='My map')

for lt, ln, el in zip(lat,lon, elev):
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el) + " m",icon = folium.Icon(color = color_producer(el), name = 'circle')))
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = str(el) + " m", 
                                     fill_color = color_producer(el), color = 'black', fill_opacity = 0.7))
    
map.add_child(fg)

#This saves the map to an html format
map.save("Map5.html")

