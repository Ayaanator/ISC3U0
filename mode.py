"""Finding the mode of a data set"""

__author__ = "Ayaan Adrito"

def mode(data: list) -> list:
    """Return a list of the modes in data.
    
    >>> mode([1, 2, 3, 4, 5])
    []

    >>> mode([1, 2, 3, 3, 4])
    [3]

    >>> mode([1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 7])
    [4, 5]
    """

    dictionary = {}
    result = []

    for num in data:
        dictionary[num] = dictionary.setdefault(num, 0) + 1

    max_occurrences = max(dictionary.values())

    if max_occurrences != min(dictionary.values()):
        for i in dictionary.keys():
            if dictionary[i] == max_occurrences:
                result.append(i)

    return result

def main():
    print(mode([1, 2, 3, 3, 4, 4, 5]))

if __name__ == "__main__":
    main()