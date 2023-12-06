#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:21:46 2020

@author: jovillal

Managing layers in folium
"""
import folium
import pandas  #use this to read a csv file

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
map = folium.Map(location=[38.58,-99.09], zoom_start = 3, tiles = "Stamen Terrain")


fgV = folium.FeatureGroup(name='Volcanos') #Use one feature group per layer
#Now add features, use zip to iterate over several lists
for lt, ln, el in zip(lat,lon, elev):
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el) + " m",icon = folium.Icon(color = color_producer(el), name = 'circle')))
    fgV.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = str(el) + " m", 
                                     fill_color = color_producer(el), color = 'black', fill_opacity = 0.7))
    
map.add_child(fgV)

fgP = folium.FeatureGroup(name='Population') 
fgP.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red' }))
  
map.add_child(fgP)


map.add_child(folium.LayerControl()) #always put this after adding the feature groups

#This saves the map to an html format
map.save("Map7.html")

