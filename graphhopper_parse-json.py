import urllib.parse
import requests
from termcolor import colored
from utils import *
from globals import *
from features.routing import *
from features.geocoding import *

def choose_vehicle():
    print(colored("\n▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    print(bold_text("Vehicle profiles available on Graphhopper:"))
    print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    print(bold_text("Available vehicles: "), end="")
    for index, vehicle in enumerate(available_vehicles):
        print(colored(vehicle, "green"), end=(", " if index != len(available_vehicles) - 1 else "\n"))
    print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    vehicle = input(bold_text("Enter a vehicle profile from the list above: "))
    if vehicle == "quit" or vehicle == "q":
        exit()
    elif vehicle.lower() in available_vehicles:
        vehicle = vehicle
    else:
        vehicle = "car"
        print("No valid vehicle profile was entered. Using the car profile.", end="\n\n")
    print(bold_text("Selected vehicle: "), end="")
    print(colored(vehicle.capitalize(), "green"), end="\n\n")
    return vehicle

while True:
    vehicle = choose_vehicle()

    print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️GEOLOCATIONS START▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")))
    orig = find_geocoding(bold_text("Starting Location: "))
    dest = find_geocoding(bold_text("Destination: "))
    print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️GEOLOCATIONS END▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")), end="\n\n")

    routing(orig, dest, vehicle)
