"""
Replace the contents of this module docstring with your own details
Name: Rhys Simpson
Date started: 24/08/2020
GitHub URL:
"""

FILENAME = "places.csv"


def main():
    """ """
    print("Travel Tracker 1.0 - by Rhys Simpson")
    in_file = open(FILENAME, "r")
    number = len(list(in_file))
    print("{} places loaded from places.csv".format(number))
    menu = "Menu:\nL - List Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
    print(menu)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            places = get_places()
            print_places(places)
        elif choice == "A":
            print("add")
        elif choice == "M":
            print("mark")
        else:
            print("Invalid Menu Choice")
        # print(menu)
        # choice = input(">>>").upper()
    print("Have a nice day")


def get_places():
    places = []
    in_file = open(FILENAME)
    for line in in_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        places.append(parts)
    in_file.close()
    return places


def print_places(places):
    """     """
    for i in places:
        print("{}. {} in {} priority {}".format(i, places[0], places[1], places[2]))


if __name__ == '__main__':
    main()
