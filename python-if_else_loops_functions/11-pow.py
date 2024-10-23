#!/usr/bin/python3
def pow(a, b):
    # Handle the case of negative exponent
    if b < 0:
        return 1 / (a ** -b)  # Return the reciprocal for negative powers
    else:
        return a ** b  # Return a raised to the power of b
