import urllib.parse
import requests
from termcolor import colored

api_key="9ceabc90-953e-42e9-a7af-26b11f91c2c9"
route_url = "https://graphhopper.com/api/1/route?"
available_vehicles = ["car", "bike", "foot"]

directions_icon = {
    "left": "⬅ ",
    "right": "⮕ ",
    "Continue": "⬆ ",
    "Arrive": "🏁",
}

status_to_color = {
    200: "green",
    400: "red",
}

def bold_text(text):
    return '\033[1m' + text + '\033[0m'

def format_directions(instruction):
    for key, value in directions_icon.items():
        if key in instruction:
            print(colored(value, "green"), end="")
            break

def geocoding (location):
    while location == "":
        location = input("Enter the location again: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1",
    "key": api_key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""

        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""

        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        # (Location Type: " + value + ")\n" + url
        print(bold_text("Found geocode: "), end=" ")
        print(colored(bold_text(new_loc), "green"), end="\n\n")
    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])
    return json_status,lat,lng,new_loc

def choose_vehicle():
    print(colored("\n▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    print("Vehicle profiles available on Graphhopper:")
    print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    print("Available vehicles: ", end="")
    for index, vehicle in enumerate(available_vehicles):
        print(bold_text(colored(vehicle, "green")), end=(", " if index != len(available_vehicles) - 1 else "\n"))
    print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white"))
    vehicle = input("Enter a vehicle profile from the list above: ")
    if vehicle == "quit" or vehicle == "q":
        exit()
    elif vehicle.lower() in available_vehicles:
        vehicle = vehicle
    else:
        vehicle = "car"
        print("No valid vehicle profile was entered. Using the car profile.", end="\n\n")
    print(bold_text("Selected vehicle: "), end="")
    print(bold_text(colored(vehicle.capitalize(), "green")), end="\n\n")
    return vehicle

def find_geocoding(text):
    loc = input(text)
    if loc == "quit" or loc == "q":
        exit(0)
    return geocoding(loc)

while True:
    vehicle = choose_vehicle()

    print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️GEOLOCATIONS START▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")))
    orig = find_geocoding(bold_text("Starting Location: "))
    dest = find_geocoding(bold_text("Destination: "))
    print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️GEOLOCATIONS END▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")), end="\n\n")

    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key": api_key, "vehicle": vehicle}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print(bold_text("Routing API Status: " + colored(str(paths_status), status_to_color[paths_status])), end="\n\n")
        if paths_status == 200:
            print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️ROUTING START▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")))
            miles = (paths_data["paths"][0]["distance"])/1000/1.61
            km = (paths_data["paths"][0]["distance"])/1000
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60) 
            print(bold_text("Distance Traveled: ") +  "{0:.1f} miles / {1:.1f} km".format(miles, km))
            print(bold_text("Trip Duration: ") + "{0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "green"))
            print(colored(bold_text("🔰 DIRECTIONS"), "white"), end="\n\n")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                instruction = " {0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, distance/1000/1.61)
                format_directions(instruction)
                print(instruction)
            print(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "green"))
            print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️ROUTING END▪▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "white")), end="\n\n")
        else:
            print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️ERROR▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "red")))
            print("Error message: " + paths_data["message"])
            print(bold_text(colored("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️ERROR▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️", "red")))
