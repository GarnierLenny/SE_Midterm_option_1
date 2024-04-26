import urllib.parse
from utils import *
from globals import *
import requests
from termcolor import colored
import json
import os

def ask_save_favorite(orig, dest, vehicle):
  answer = input(bold_text(colored("⭐ Save this trip to favorites? ", "light_yellow") + colored("(yes/no): ", "dark_grey")))
  if answer.lower() == "yes":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, "data.json")
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
    print(bold_text(colored("✅ Successfully saved trip to favorites!", "green")))
  else:
    print(colored("Trip not saved to favorites", "dark_grey"))
