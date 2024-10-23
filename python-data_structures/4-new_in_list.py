#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list.copy()
                
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return new_list  # Return the copy unchanged

    # Replace the element at the specified index
        new_list[idx] = element
        return new_list  # Return the modified copy
