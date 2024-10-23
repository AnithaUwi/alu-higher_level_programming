#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0

 # Check if there are arguments
    if len(sys.argv) == 1:
        print(0)  # No arguments passed
    else:
     # Sum the arguments, convert to integer
        for arg in sys.argv[1:]:
            total += int(arg)  # Convert argument to integer and add to total

            print(total)  # Print the total sum

