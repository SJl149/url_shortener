import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def greeting():
    clear_screen()
    print("###  Welcome to URLShorter!  ###\n")


def quit_program():
    print("\nThank you for using URLShorter!\n\n")
    exit()


def print_menu():
    print("\nMenu:")
    print("    1. Add URL")
    print("    2. Find long URL")
    print("    3. Get stats on number of times a short URL was clicked")
    print("    4. Delete URL")
    print("    5. Quit\n")


def get_menu_choice():
    choice = input("Select option: ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 5:
        print("\nInvalid choice: please enter a number from 1-5!\n")
        choice = input("     Please enter a number from the above menu: ")
    return choice


def ask_to_continue():
    response = input("\nPress <return> to continue or enter <quit> to exit: ")
    if response in ["quit", "q", "Q"]:
        return False
    else:
        return True


def enter_new_url():
    long_url = input("\nEnter long URL to add: ")
    while len(long_url) < 1:
        long_url = input("\n     Please enter a URL with length greater than 1: ")
    custom_key = input("\nEnter a custom key or press <return> to randomly generate key: ")
    while custom_key != "" and len(custom_key) > 6:
        print("\n     Custom keys must be strings of 6 alphanumeric characters (ex: abc123)")
        custom_key = input("\nEnter a custom key or press <return> to randomly generate key: ")
    return long_url, custom_key


def enter_short_url_key():
    key = input("\nEnter shortened URL key (ex: abc123 from urlshorter/abc123) to find original: ")
    while len(key) != 6:
        key = input("\n    Invalid key. Please enter the last 6 characters from the shortened URL: ")
    return key
