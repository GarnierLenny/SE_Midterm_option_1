import urllib.parse
import requests
from termcolor import colored
from utils import *
from .geocoding import *
from .favorite import *

def favorite(args):
  if args[1] == "-l":
    show_favorite_list()
  elif int(args[1]) != 0:
    load_trip(int(args[1]))
  else:
    print(bold_text(colored("Invalid or missing option", "grey")))

def load_trip(trip_to_load):
  data = load_json()
  if trip_to_load <= 0 or trip_to_load > len(data):
    print(bold_text(colored("Trip number out of range, please try again", "red")), end="\n\n")
    return
  print()
  route(data[trip_to_load - 1]['orig'], data[trip_to_load - 1]['dest'], data[trip_to_load - 1]['vehicle'], [], False)

def choose_vehicle():
    print(bold_text("\nAvailable vehicles: "), end="")
    for index, vehicle in enumerate(available_vehicles):
        print(colored(vehicle, "green"), end=(", " if index != len(available_vehicles) - 1 else "\n"))
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

def route(orig, dest, vehicle, stops, save):
    for stop in stops:
        if stop[0] != 200:
            return
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        sts = ""
        for stop in stops:
            sts += "&point=" + str(stop[1]) + "%2C" + str(stop[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key": api_key, "vehicle": vehicle}) + op + sts + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print(bold_text("Routing API Status: " + colored(str(paths_status), status_to_color[paths_status])), end="\n\n")
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"])/1000/1.61
            km = (paths_data["paths"][0]["distance"])/1000
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60) 
            print(bold_text("Distance Traveled: ") +  "{0:.1f} miles / {1:.1f} km".format(miles, km))
            print(bold_text("Trip Duration: ") + "{0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print(bold_text("Height difference: ") + "{0:.1f} m".format(paths_data["paths"][0]["ascend"]+paths_data["paths"][0]["descend"]))
            print(colored(bold_text("🔰 DIRECTIONS"), "white"), end="\n\n")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                instruction = " {0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, distance/1000/1.61)
                format_directions(instruction)
                print(instruction)
            if save == True:
                ask_save_favorite(orig, dest, vehicle)
        else:
            print(colored(paths_data["message"], "red"), end="\n\n")

def trip(args):
    vehicle = choose_vehicle()
    stops = []
    orig = find_geocoding(bold_text("Starting Location: "))
    while True:
        answer = input(bold_text(colored("Add a stop? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
        if answer == "yes":
            stops.append(find_geocoding(bold_text("Stop to add: ")))
        else:
            break
    answer1 = input(bold_text(colored("Round trip? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
    answer2 = input(bold_text(colored("Keep stops? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
    if answer1 == "yes":
        stops.reverse()
        route(dest, orig, vehicle, (stops if answer2 == "yes" else []), True)
    else:
        dest = find_geocoding(bold_text("Destination: "))
        route(orig, dest, vehicle, stops, True)