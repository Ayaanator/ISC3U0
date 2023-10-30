"""Coding solution for in class coding assignment"""

__author__ = "Ayaan Adrito"

def valid_number(s):
    """Determines the validity of a credit card number"""
    result = ""
    sum = 0

    #Double the number every two digits
    for i in range(len(s)):
        if i % 2 == 0:
            result += str(int(s[i])*2)
        else:
            result += s[i]

    for letter in result:
        sum += int(letter)

    if sum % 10 == 0:
        print(f"The digit {s} is valid.")
    else:
        print(f"The digit {s} is NOT valid.")

def main():
    """The main program"""

    number = str(input("Enter your number: "))
    
    valid_number(number)

if __name__ == "__main__":
    main()
