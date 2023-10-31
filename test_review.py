'''Test review for Tuesday, October 31st'''

def string_cutter(s):
    return s[1:-1]

def exchange_letters(s):
    return s[-1] + s[1:-1] + s[0]

def next_char(s):
    if ord(s) == 90 or ord(s) == 122:
        return chr(ord(s) - 25)
    else:
        return chr(ord(s) + 1)

def pig_latin(s):
    return s[1:] + s[0] + "ay"

def box_sides(length, width, height):
    Big_side = length*height
    Small_side = width*height
    return 2*(Big_side + Small_side)

def f(big, small):
    total = big + small
    return total - big

def upper_lower(s):
    string = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            if i < len(s) / 2:
                string += chr(ord(s[i]) - 32)
            else:
                string += s[i]
        else:
            string += s[i]

    return string

def main():
    test = upper_lower("hi")
    print(test)

if __name__ == "__main__":
    main()