#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list unchanged
    my_list[idx] = element  # Replace the element at the specified index
    return my_list  # Return the modified list
