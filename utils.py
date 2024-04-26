from termcolor import colored
from globals import *

def bold_text(text):
    return '\033[1m' + text + '\033[0m'

def format_directions(instruction):
    for key, value in directions_icon.items():
        if key in instruction:
            print(colored(value, "green"), end="")
            break