from utils import bold_text, colored

def help(args):
    print(bold_text(colored("\nGraphhopper manual:", "green")))
    print(bold_text("help\t\t\t\t"), end="")
    print("Show command list")
    print(bold_text("trip\t\t\t\t"), end="")
    print("Calculate trip directions")
    print(bold_text("favorite [-l/{trip_number}]\t"), end="")
    print("Locate a place / Find the location of a treasure")
    print(bold_text("locate [location/treasure]\t"), end="")
    print("Find location/treasure")
    print(bold_text("exit\t\t\t\t"), end="")
    print("Exit graphhopper")
    print()