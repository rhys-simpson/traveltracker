"""
Replace the contents of this module docstring with your own details
Name: Rhys Simpson
Date started: 24/08/2020
GitHub URL:
"""

from operator import itemgetter
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
        places.sort(key=itemgetter(3, 2))
    in_file.close()
    return places


def print_places(places):
    """     """
    number = 0
    unvisited_places = []
    for places_data in places:
        if places_data[3] == "n":
            unvisited = "*"
            number += 1
            print("{:2}{}. {} in {} priority {}".format(unvisited, number, *places_data[:-1]))
            unvisited_places.append(unvisited)
        else:
            number += 1
            print("{:3}. {} in {} priority {}".format(number, *places_data[:-1]))
    print("{} places. You still need to visit {} places.".format(len(list(places)), len(unvisited_places)))


if __name__ == '__main__':
    main()
