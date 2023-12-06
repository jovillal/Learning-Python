#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:59:28 2020

@author: jovillal

Build a map in html
Maps can be build using folium (this is a java script, css, and html translator)
"""

import folium

#This creates a map object, the location is in latitude and longitude, think of this as a layer
map = folium.Map(location=[5,-74])

#This saves the map to an html format
map.save("Map1.html")

#Use a different tile set (¿?)
map = folium.Map(location=[38.58,-99.09], zoom_start = 6, tiles = "Stamen Terrain")

#To add a marker (more layers?)
map.add_child(folium.Marker(location=[38.2,-99.1], popup="A marker",icon = folium.Icon(color = 'green')))

map.save("Map2.html")


#To add a feature group (many things on a single layer?)
map = folium.Map(location=[38.58,-99.09], zoom_start = 9, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My map')
fg.add_child(folium.Marker(location=[38.2,-99.1], popup="A marker",icon = folium.Icon(color = 'green'))) #do this many times, inside a for loop for example
fg.add_child(folium.Marker(location=[38.3,-99.0], popup="A red marker",icon = folium.Icon(color = 'red')))

map.add_child(fg)

map.save("Map3.html")

