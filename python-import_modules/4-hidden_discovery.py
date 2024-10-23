#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the modul
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort the names in alphabetical order
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)
