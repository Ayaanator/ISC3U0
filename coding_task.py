"""Credit Card Number Checker: This program takes a number as an input.

It then either validates it or generates a check digit."""

__author__ = "Ayaan Adrito"

def number_sum(s):
    """Multiply every two digit by two and return the sum of each digit"""

    result = ""
    total = 0

    #Double the number every two digits
    for i in range(len(s)):
        if i % 2 == 0:
            result += str(int(s[i])*2)
        else:
            result += s[i]

    #Add each digit to check if it is a multiple of 10
    for letter in result:
        total += int(letter)

    return total

def valid_number(s):
    """Determine the validity of a credit card number."""
    
    total = number_sum(s)
 
    if total % 10 == 0:
        print(f"The digit {s} is valid.")
    else:
        print(f"The digit {s} is NOT valid.")

def check_digit(s):
    """Calculate and return the check digit."""
    total = number_sum(s)
    result = (10 - w_sum % 10) % 10

    #Add the check digit to the end of the input
    new_digit = s + str(result)
    
    print(f"The check digit of {s} is {result}. The new digit is {new_digit}.")

def arbitrary_number(s):
    """Determine if an arbitrary value is valid.

    If not, then calculate the check digit and print a new arbitrary value."""

    total = number_sum(s)
    print(total)

    if total % 10 == 0:
        print(f"The digit {s} is valid.")
    else:
        result = 0
        nearest_ten = total // 10
        
        if len(s) == 0:
            result = (nearest_ten - total) / 2
        else:
            result = nearest_ten - total

        #Add check digit to arbitrary number
        new_digit = s + str(result)
    
        print(f"The check digit of {s} is {result}. The new digit is {new_digit}.")

def main():
    """The main program."""

    number = str(input("Enter your number: "))
  
    if len(number) == 16:
        valid_number(number)
    elif len(number) == 15:
        check_digit(number)
    else:
        arbitrary_number(number)

if __name__ == "__main__":
    main()
