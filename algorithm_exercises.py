"""Learning lists and algorithms!"""

__author__ = "Ayaan Adrito"

def my_min(my_list: list) -> any:
    """Find and return the smallest value in list.
    
    >>> my_min(['hello', 'NINE', 'Trees'])
    'NINE'

    >>> my_min([1, 2, 4, 5, 3, 5])
    1
    """

    smallest_item = my_list[0]
    for item in my_list:
        if item < smallest_item:
            smallest_item = item

    return smallest_item

def find(my_list: list, searched_value) -> int:
    """Return the index of searched_value in my_list. 
    If value is not found, return -1
    
    >>> find([1, 2, 4, 5, 3, 5], 3)   
    4

    >>> find(['dbz', 'mha', 'jjk', 'jjba', 'aot'], 'dbz') 
    0

    >>> find(['mkx', 'mk11', 'sfv', 'sf6', 'dbfz'], 'ggst') 
    -1
    """

    for i in range(len(my_list)):
        if my_list[i] == searched_value:
            return i

    return -1

def print_max(my_list: list):
    """Find index of the largest value in my_list and print them."
    
    >>> print_max()
    """

    for i in range(len(my_list)):
        if my_list[i] == searched_value:
            print(f"The value {my_list[i]} is at index {i}")

def main():
    print("my fellow")

if __name__ == "__main__":
    main()
