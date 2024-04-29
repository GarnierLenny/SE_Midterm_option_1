import urllib.parse
import requests
from termcolor import colored
from utils import *
from globals import *
from features.routing import *
from features.geocoding import *
from features.favorite import *
from features.help import *

commands = {
    "help": help,
    "trip": trip,
    "favorite": favorite,
    "exit": exit,
}

print(bold_text(colored("\nWelcome to Graphhopper! type 'help' to see the command list", "light_cyan")), end="\n\n")

while True:
    text = input(bold_text(colored("Graphhoper $> ", "light_magenta"))).strip().split(" ")

    if text[0] in commands:
        commands[text[0]](text)
    else:
        print(colored("Unknown command '" + text[0] + "'", "grey"), end="\n\n")