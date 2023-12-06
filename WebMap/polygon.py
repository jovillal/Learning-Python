#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:40:07 2020

@author: jovillal

Adding polygons to maps, via a json file
"""

import folium

#This creates a map object, the location is in latitude and longitude, think of this as a layer
map = folium.Map(location=[38.58,-99.09], zoom_start = 3, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My map')

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red' }))

map.add_child(fg)
map.save("Map6.html")

