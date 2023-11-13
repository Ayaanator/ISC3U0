"""Assignment04: Lists, Functions, and the Function Design Recipe

Complete the code below as required with proper formatting.

Instructions follow the format #n.

When completed correctly, the output should appear exactly as below.

DO NOT alter the main() function, but definitely read it to aid you in
completing the function code.

<BEGIN SAMPLE OUTPUT>

    Something About Strings

    Enter 5 strings:
    > hello
    > hej
    > ciao
    > annyeong
    > bonjour

    You entered:
    index 0: hello
    index 1: hej
    index 2: ciao
    index 3: annyeong
    index 4: bonjour

    Enter a minimum length: r
    Invalid input...
    Enter a minimum length: 4
    Strings longer than 4:
    hello
    annyeong
    bonjour

    The average length: 5.4
    The longest string is: annyeong

<END SAMPLE OUTPUT>

"""

#1 Complete the HEADER of this function (including type contract).
def get_int(msg: str) -> int:
    """Return an int gotten from the user with input message msg.

    Validate input so that only integers are accepted."""
    
    while True:
        try:
            x = int(input(msg))
            return x
        except ValueError:
            print('Invalid input...')
            

#2 Complete the DESCRIPTION of this function.
def get_list_of_strings(n: int) -> [str]:
    """Create and return strings list from user input of n strs."""
    strings = []
    for i in range(n):
        strings.append(input('> '))
    return strings


#3 Complete the DESCRIPTION and BODY of this function.
def average_length(strs: [str]) -> float:
    """Return average length of strings in list strs.

    >>> average_length(['hi', 'hello'])
    3.5
    >>> average_length([])
    0
    """

    total = 0

    for word in strs:
        total += len(word)

    return total / len(strs)

#4 Complete the HEADER and BODY of this function.
def print_items(strs: [str]):
    """Print the things in items nicely labelled with index numbers.

    If the list is empty, print 'No items!'.
    """

    if len(strs) == 0:
        print("No items!")
    else:
        for i in range(len(strs)):
            print(f"index {i}: {strs[i]}")

#5 Complete the BODY of this function.
def print_long_strings(strs: [str], minimum: int):
    """Print only the strings in strs that are strictly longer than minimum.

    Print all items on their own line. If there are no strings to print,
    print 'No items!'.
    """
    printed = False

    # Find and print words longer than minimum
    for word in strs:
        if len(word) > minimum:
            if printed == False:
                printed = True
                print(f"Strings longer than {minimum}: ")
            print(word)
        
    # Run if there are no word longer than minimum
    if printed == False:
        print("No items!")
        
#6 Complete the DESCRIPTION, EXAMPLES, and BODY of this function.
def longest_string(strs: [str]) -> str:
    """Return the longest string in list strs.
    
    >>> longest_string(['banana', 'carrot', 'apple'])
    'banana'

    >>> longest_string(['hello', 'rectangle', 'child'])
    'rectangle'
    """

    if len(strs) == 0:
        return ""

    longest_index = 0

    # Compare strings and set index to longest string
    for i in range(1, len(strs)):
        if len(strs[i]) > len(strs[longest_index]):
            longest_index = i
        
    return strs[longest_index]
    
##-- DO NOT ALTER ANY CODE BELOW THIS LINE (YOU MAY COMMENT LINES)--##
def main():
    NUM_STRINGS = 5
    print('Something About Strings\n')
    print('Enter', NUM_STRINGS, 'strings:')
    strings = get_list_of_strings(NUM_STRINGS)
    print('\nYou entered:')
    print_items(strings)
    print()
    cut = get_int('Enter a minimum length: ')
    print_long_strings(strings, cut)
    avg = average_length(strings)
    print('\nThe average length: {:.1f}'.format(avg))
    print('The longest string is:', longest_string(strings))
    

if __name__ == '__main__':
    main()
