#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for the number of elements printed

    try:
        # Iterate over the elements of the list
        for i in range(x):
            print(my_list[i], end=' ')
            count += 1
    except IndexError:
        pass  # Handle the exception when the index is out of range

    print()  # Print a new line after the elements
    return count
