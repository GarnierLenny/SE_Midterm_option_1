from .geocoding import *
from termcolor import colored
from utils import *
import requests
from urllib.parse import urlencode
import random

# find coord of a location
def find_coords():
    loc = input("Enter the location: ")
    if loc == "quit" or loc == "q":
        exit(0)
    coord = geocoding(loc)
    print(bold_text("Found coordinates:"), end=" ")
    print(colored(bold_text(str(coord[1]) + ", " + str(coord[2])), "green"), end="\n\n")
    return

# game like find the number
def find_treasure():
    loop = True
    print("The goal is to find the treasure by guessing the coordinates !")
    print("Enter the coordinates in the format 'latitude longitude' or type 'quit' to exit.")
    treasure = [random.uniform(0, 90), random.uniform(0, 180)]
    while loop:
        cmd = input("Enter coordinates: ")
        if cmd == "quit" or cmd == "q":
            exit(0)
        lat, lng = cmd.split(" ")
        if abs(float(lat) - treasure[0]) <= 0.1 and abs(float(lng) - treasure[1]) <= 0.1:
            print(colored(bold_text("Congratulations! You found the treasure!"), "green"), end="\n\n")
            loop = False
        else:
            if abs(float(lat) - treasure[0]) > 0.1:
                print(colored(bold_text("Latitude is higher"), "yellow"))
            else:
                print(colored(bold_text("Latitude is lower"), "yellow"))
            if abs(float(lng) - treasure[1]) > 0.1:
                print(colored(bold_text("Longitude is higher"), "yellow"), end="\n\n")
            else:
                print(colored(bold_text("Longitude is lower"), "yellow"), end="\n\n")