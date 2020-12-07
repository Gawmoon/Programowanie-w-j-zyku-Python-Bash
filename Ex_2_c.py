#!/usr/bin/env python



from PIL import Image

def convert_to_png(file_path):
    jpg = Image.open(file_path)
    jpg.save(file_path[0:len(file_path)-3]+"png", "PNG")

file="JPG1.jpg"
convert_to_png(file)
