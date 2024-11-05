# _Utiles grales para la app
import os

def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # clear_console()
    print("\n--- TODO List Menu ---")
    print("1. Add TODO")
    print("2. View TODOs")
    print("3. Update TODO")
    print("4. Delete TODO")
    print("0. Exit")

#