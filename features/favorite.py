import urllib.parse
from utils import *
from globals import *
import requests
from termcolor import colored
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory, "data.json")

def load_json():
  file = open(path, "r")
  data = json.load(file)['favorite_trips']
  return data

def show_favorite_list():
  data = load_json()
  for index, trip in enumerate(data):
    print(underline_text(bold_text("Trip no." + str(index + 1) + ":")))
    print(bold_text(colored("Start:\t\t", "cyan") + trip['orig'][3]))
    print(bold_text(colored("End:\t\t", "cyan") + trip['dest'][3]))
    print(bold_text(colored("Vehicle:\t", "cyan") + trip['vehicle'].capitalize()), end="\n\n")

def ask_load_favorite():
  answer = input(bold_text(colored("⭐ Load favorite trip? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
  print()
  if answer.lower() == "yes":
    show_favorite_list()
    return True
  return False

def ask_save_favorite(orig, dest, vehicle):
  answer = input(bold_text(colored("\n⭐ Save this trip to favorites? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
  if answer.lower() == "yes":
    file = open(path, "r")
    data = json.load(file)
    new_favorite = {
      "orig": orig,
      "dest": dest,
      "vehicle": vehicle,
    }
    data['favorite_trips'].append(new_favorite)
    file = open(path, 'w')
    json.dump(data, file, indent=2)
    print(bold_text(colored("✅ Successfully saved trip to favorites!", "green")), end="\n\n")
  else:
    print(colored("Trip not saved to favorites", "dark_grey"), end="\n\n")
