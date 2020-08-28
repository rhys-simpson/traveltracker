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
        print(menu)
        choice = input(">>>").upper()
    print("Have a nice day")


def get_places():
    """ """
    places = []
    in_file = open(FILENAME)
    for line in in_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        places.append(parts)
    places.sort()
    in_file.close()
    return places


def print_places(places):
    """     """
    for places_data in places:
        if places_data[3] == "n":
            unvisited = "*"
            print("{}{}. {} in {} priority {}".format(unvisited, 1, places_data[0], places_data[1], places_data[2]))
        else:
            print("{}. {} in {} priority {}".format(1, places_data[0], places_data[1], places_data[2]))
        # if places[3] == "n":
            # unvisited += 1
        # print("{} places. You still want to visit {} places.".format(len(list(places)), unvisited))


if __name__ == '__main__':
    main()
