""""
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
    """ """

    longest_country_name_length, longest_number_length, longest_town_name_length = longest_elem_length(places)

    unvisited_places = []
    for number, places_data in enumerate(places):
        if places_data[3] == "n":
            unvisited = "*"
            unvisited_places.append(unvisited)
        else:
            unvisited = ""
        print("{:1}{}. {:<{}} in {:<{}} priority {:>{}}".format(unvisited, number+1, places_data[0],
                                                                longest_town_name_length, places_data[1],
                                                                longest_country_name_length, places_data[2],
                                                                longest_number_length))
    print("{} places. You still want to visit {} places.".format(len(list(places)), len(list(unvisited_places))))


def longest_elem_length(places):
    """ """
    longest_town_name_length = 0
    longest_town_name = [places_data[0] for places_data in places if len(places_data) > longest_town_name_length]
    for word in longest_town_name:
        if len(word) > longest_town_name_length:
            longest_town_name_length = len(word)
    longest_country_name_length = 0
    longest_country_name = [places_data[1] for places_data in places if len(places_data) > longest_country_name_length]
    for word in longest_country_name:
        if len(word) > longest_country_name_length:
            longest_country_name_length = len(word)
    longest_number_length = 0
    longest_number = [places_data[2] for places_data in places if len(places_data) > longest_number_length]
    for word in longest_number:
        if len(str(word)) > longest_number_length:
            longest_number_length = len(str(word))
    return longest_country_name_length, longest_number_length, longest_town_name_length


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
    print("Enter the number of a place to mark as visited")
    finished = False
    while not finished:
        try:
            item_to_change = int(input(">>> "))
            if item_to_change < 0:
                print("Number must be > 0")
            elif item_to_change > len(list(places)):
                print("Invalid place number")
            elif places[item_to_change - 1][3] == "v":
                print("That place is already visited")
            else:
                finished = True
                places[item_to_change - 1][3] = "v"
                print("{} in {} visited!".format(places[item_to_change - 1][0], places[item_to_change - 1][1]))
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
