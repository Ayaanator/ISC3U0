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
    
    >>> print_max(['dbz', 'mha', 'jjk', 'jjba', 'aot']) 
    The value mha is at index 1

    >>> print_max([5, 12, 643, 23, 4])
    The value 643 is at index 2
    """
    max_index = 0
    max_value = my_list[max_index]
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_index = i
            max_value = my_list[max_index]
        
    print(f"The value {max_value} is at index {max_index}")

def print_min(my_list: list):
    """Find index of the smallest value in my_list and print them."
    
    >>> print_min(['dbz', 'mha', 'jjk', 'jjba', 'aot'])
    The value aot is at index 4

    >>> print_min([5, 12, 643, 23, 4])
    The value 4 is at index 4
    """
    min_index = 0
    min_value = my_list[min_index]
    for i in range(len(my_list)):
        if my_list[i] < min_value:
            min_index = i
            min_value = my_list[min_index]
        
    print(f"The value {min_value} is at index {min_index}")

def placer(my_list: list, searched_value) -> int:

def main():
    print("my fellow")

if __name__ == "__main__":
    main()
