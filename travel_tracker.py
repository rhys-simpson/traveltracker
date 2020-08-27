"""
Replace the contents of this module docstring with your own details
Name: Rhys Simpson
Date started: 24/08/2020
GitHub URL:
"""


def main():
    print("Travel Tracker 1.0 - by Rhys Simpson")
    in_file = open("places.csv", "r")
    number = len(list(in_file))
    print("{} places loaded from places.csv".format(number))
    menu = "Menu:\nL - List Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
    print(menu)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            print("l")
        elif choice == "A":
            print("add")
        elif choice == "M":
            print("mark")
        else:
            print("Invalid Menu Choice")
        print(menu)
        choice = input(">>>").upper()
    print("Have a nice day")


if __name__ == '__main__':
    main()
