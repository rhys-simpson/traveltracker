""""
Name: Rhys Simpson
Date started: 27/08/2020
GitHub URL: https://github.com/rhys-simpson/traveltracker
"""

from operator import itemgetter
FILENAME = "places.csv"


# TODO add print statements; formatting etc. to match sample output
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
    save_places(places)


def change_visited_number(places):
    visit = 0
    for places_data in places:
        if places_data[3] == "n":
            visit += 1
    return visit


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


def print_places(places):
    """ """

    longest_country_name_length, longest_number_length, longest_town_name_length = longest_elem_length(places)

    visit = change_visited_number(places)
    places.sort(key=itemgetter(3, 2))
    for number, places_data in enumerate(places):
        if places_data[3] == "v":
            unvisited = ""
        else:
            unvisited = "*"
        print("{:1}{}. {:<{}} in {:<{}} priority {:>{}}".format(unvisited, number+1, places_data[0],
                                                                longest_town_name_length, places_data[1],
                                                                longest_country_name_length, places_data[2],
                                                                longest_number_length))
    if visit <= 0:
        print("{} places. No places left to visit. Why not add a new place?".format(len(list(places))))
    else:
        print("{} places. You still want to visit {} places.".format(len(list(places)), visit))


def longest_elem_length(places):
    """ """
    longest_town_name_length = max(len(places_data[0]) for places_data in places)
    longest_country_name_length = max(len(places_data[1]) for places_data in places)
    longest_number_length = max(len(str(places_data[2])) for places_data in places)
    return longest_country_name_length, longest_number_length, longest_town_name_length


def add_place(places):
    """ """
    name, country, priority = get_valid_input()
    new_place = [name, country, priority, "n"]
    places.append(new_place)


def get_valid_input():
    """ """
    finished = False
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country == "":
        print("Input can not be blank")
        country = input("Country: ")
    while not finished:
        try:
            priority = int(input("Priority: "))
            while priority < 0:
                print("Number must be > 0")
                priority = int(input("Priority: "))
            else:
                finished = True
                print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
                return name, country, priority
        except ValueError:
            print("Invalid input; enter a valid number")


def mark_visited(places):
    """ """
    finished = False
    visit = change_visited_number(places)
    if visit == 0:
        print("No unvisited places")
        finished = True

    while not finished:
        print_places(places)
        print("Enter the number of a place to mark as visited")
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


def save_places(places):
    """ """
    out_file = open("places.csv", "w")
    for places_data in places:
        print("{},{},{},{}".format(places_data[0], places_data[1], places_data[2], places_data[3]), file=out_file)
    out_file.close()
    print("{} places saved to places.csv".format(len(list(places))))
    print("Have a nice day :)")


if __name__ == '__main__':
    main()
