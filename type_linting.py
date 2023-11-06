"""Learning how to type lint!"""

def is_even(n: int) -> bool:
    """Retrun True if value n is divisible by 2
    
    >>> is_even(4)
    True
    >>> is_even(17)
    False
    """
    
    return n % 2 == 0

def repeat_word(word: str, count: int) -> str:
    """Return word repeated count times
    
    >>> repeat_word('Marcia', 3)
    'Marcia Marcia Marcia'
    """

def main():
    print(is_even(4))

if __name__ == "__main__":
    main()