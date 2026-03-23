def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_char_separator(char):
    print(char * 30)

def print_custom_separator(char, length):
    if length <=0:
        print("")
        return
    print(char * length)

def print_labeled_separator(label, char="*", width=30):
    print(label.center(width, char))

def print_box(message, char="*"):
    width = len(message) + 4
    print(char * width)
    print(char + " " + message + " " + char)
    print(char * width)

c = {
    "white": "\033[97m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "reset": "\033[0m" 
}
def print_fishing():
    lines = [
    r"                  ////\\\ ",
    r"                 /////\\\\ ",
    r"                //__   __\\ ",
    r"               -| (o \ o) |- ",
    r"              |d|   c_\   |b| ",
    r"               -\((\___/))/-                       ___ ",
    r"                 \ \___/ /                      ||//// ",
    r"                  \_____/                       | uuu ",
    r"                  |     |                      /\ _/ ",
    r"                  /\ ) /\                     /  V | ",
    r"          _______/\ \ / /\_______            /  /  | ",
    r"         /         \/V\/         \          /\ /  /V\ ",
    r"        /           |o|           \        /\ V  |  o\ ",
    r"       /            | |            \      /  \/\ //###| ",
    r"      /             |o|             \    /   /o/ |####|> ",
    r"     /              | |              \  /   / / <|####|> ",
    r"    /               |o|   _____       \/    \/    \##/ ",
    r"   /                | |   |   |             /     |##| ",
    r"  /       /         |o|   |   |  \         /     /_/\_\ ",
    r" /       /|         | |   |___|  |\       / ",
    r"/       / |         |o|          | \_____/ "
]
    for i in range(0,3):
        print(f"{c['blue']}{lines[i]}{c['reset']}")
    for i in range(3, 9):
        print(f"{c['yellow']}{lines[i]}{c['reset']}")
    for i in range(9, 21):
        print(f"{c['green']}{lines[i]}{c['reset']}")
