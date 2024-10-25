#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
                    
    max_value = my_list[0]  # Initialize max_value with t
    for num in my_list:      # Iterate through each numb
            if num > max_value:  # Compare with max_value
                max_value = num   # Update max_value if 
                                                        
    return max_value
