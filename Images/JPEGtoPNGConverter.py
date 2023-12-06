""" 
A script that takes two arguments: the path to a folder and the name of a new folder.
It takes all jpg from the folder, creates the new folder if needed and converts the images to png
It doesn't erase the jpg 
"""
import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

size = 128, 128

if not os.path.exists(image_folder):
	print("No image folder found.")
else:
	print ('Scaning from ' + image_folder)
	if os.path.exists(output_folder):
		print ('Writing to ' + output_folder)
	else:
		os.makedirs(output_folder)
		print ('Created ' + output_folder, os.path.exists(output_folder))
	for file in os.listdir(image_folder):
		img = Image.open(f'{image_folder}{file}')
		if img.format == 'JPEG':
			print(f"Converting {file}")
			clean_name = os.path.splitext(file)
			img.thumbnail(size)
			img.save(f'{output_folder}{clean_name[0]}.png', "PNG")




print(image_folder,output_folder)