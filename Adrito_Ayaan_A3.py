"""Coding solution for in class coding assignment."""

__author__ = "Ayaan Adrito"

def number_sum(s):
    """Double every two digit and return sum of every single digit."""

    result = ""
    total = 0

    #Double the number every two digits
    for i in range(len(s)):
        if i % 2 == 0:
            result += str(int(s[i])*2)
        else:
            result += s[i]

    for letter in result:
        total += int(letter)

    return total

def valid_number(s):
    """Determines the validity of a credit card number."""

    total = number_sum(s)

    if total % 10 == 0:
        print(f"The digit {s} is valid.")
    else:
        print(f"The digit {s} is NOT valid.")

def check_digit(s):
    """Generate check digit and output new number."""

    total = number_sum(s)
    target = (total - (total % 10)) + 10
    check_digit = target - total
    final_digit = s + str(check_digit)

    print(f"The check digit is {check_digit}. The new digit is {final_digit}.")

def arbitrary_number(s):
    """Determine validity of number. If not valid, generate check digit."""

    total = number_sum(s)
    target = (total - (total % 10)) + 10

    if total % 10 == 0:
        print(f"The digit {s} is valid.")
    else:
        if len(s) % 2 == 0:
            check_digit = (target - total) / 2
        else:
            check_digit = target - total

        final_digit = s + str(check_digit)
        print(f"The check digit is {check_digit}. The new digit is {final_digit}.")

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