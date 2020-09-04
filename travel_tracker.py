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
    places = get_places()
    number = len(list(places))
    print("{} places loaded from places.csv".format(number))
    menu = "Menu:\nL - List Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places)
        else:
            print("Invalid Menu Choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Have a nice day")


def get_places():
    places = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        places.append(parts)
        places.sort(key=itemgetter(3, 2))
    in_file.close()
    return places


# TODO sort by unvisited, add print statement (.. places. No places left to visit. Why not add a new place?)
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
    longest_town_name_length = max(len(places_data[0]) for places_data in places)
    longest_country_name_length = max(len(places_data[1]) for places_data in places)
    longest_number_length = max(len(str(places_data[2])) for places_data in places)
    return longest_country_name_length, longest_number_length, longest_town_name_length


# TODO fix so doesnt continuously loop
def add_place(places):
    """ """
    name = get_valid_input()
    country = get_valid_input()
    priority = get_valid_input()
    visited = get_valid_input()
    new_place = [name, country, priority, visited]
    places.append(new_place)


# TODO fix so doesnt continuously loop
def get_valid_input():
    """ """
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country == "":
        print("Input can not be blank")
        country = input("Country: ")
    finished = False
    while not finished:
        try:
            priority = int(input("Priority: "))
            while priority < 0:
                print("Number must be > 0")
                priority = int(input("Priority: "))
            finished = True
            VISITED = "n"
            print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
            return name, country, priority, VISITED
        except ValueError:
            print("Invalid input; enter a valid number")


# TODO add print statement for when no unvisited places (sample output)
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
                break
            else:
                finished = True
                places[item_to_change - 1][3] = "v"
                print("{} in {} visited!".format(places[item_to_change - 1][0], places[item_to_change - 1][1]))
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
