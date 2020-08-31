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
            places = get_valid_input()
            add_place(places)
        elif choice == "M":
            places = get_places()
            mark_visited(places)
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
    unvisited_places = []
    for number, places_data in enumerate(places):
        if places_data[3] == "n":
            unvisited = "*"
            print("{:2}{}. {} in {} priority {}".format(unvisited, number+1, *places_data[:-1]))
            unvisited_places.append(unvisited)
        else:
            print("{:3}. {} in {} priority {}".format(number+1, *places_data[:-1]))
    print("{} places. You still need to visit {} places.".format(len(list(places)), len(unvisited_places)))


def add_place(places):
    """ """
    name = get_valid_input()
    country = get_valid_input()
    priority = get_valid_input()
    visited = get_valid_input()
    new_place = [name, country, priority, visited]
    places.append(new_place)


def get_valid_input():
    """ """
    name = input("Name: ")
    if name == "":
        print("Input can not be blank")
        name = input("Name: ")

    country = input("Country: ")
    if country == "":
        print("Input can not be blank")
        country = input("Country: ")

    priority = int(input("Priority: "))
    if priority < 0:
        print("Number must be > 0")
        priority = int(input("Priority: "))

    visited = "n"

    print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
    return name, country, priority, visited


def mark_visited(places):
    """ """
    item_to_change = int(input("Enter the number of the place you want to change: "))
    if item_to_change < 0:
        print("Number must be > 0")
        item_to_change = int(input("Enter the number of the place you want to change: "))
    elif item_to_change > len(places):
        print("Invalid place number")
        item_to_change = int(input("Enter the number of the place you want to change: "))
    elif item_to_change == places[2]:
        print("That place is already visited")
        item_to_change = int(input("Enter the number of the place you want to change: "))
    else:
        places[item_to_change - 1][3] = "v"
    places.append(item_to_change)


if __name__ == '__main__':
    main()
