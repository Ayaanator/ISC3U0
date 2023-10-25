'''Exercises 2.3: Lists'''

__author__ = "Ayaan Adrito"

def validate_input(message):
    '''Valid user input so it is a int or float'''
    while True:
        try:
            n = float(input(message))
            return n
        except:
            print("You can't input a string!")

def get_float_list(n):
    '''Get float list and return to user'''
    
    float_list = []
    for i in range(n):
        float_list.append(validate_input(f"Enter float {i + 1}: "))
        
    return float_list

def get_int_list(n):
    '''Get int list and return to user'''
    
    int_list = []
    for i in range(n):
        int_list.append(validate_input(f"Enter int {i + 1}: "))
        
    return int_list

def get_string_list(n):
    '''Get string list and return to user'''
    
    word_list = []
    for i in range(n):
        word_list.append(input())
        
    return word_list

def mean(num_list):
    '''Returns the mean of all items of list'''        
    return sum(num_list) / len(num_list)

def length_of_strings(string_list):
    
    result = []
    
    for i in range(len(string_list)):
        result.append(len(string_list[i]))
        
    return result

def mean_length_of_strings(string_list):
    string_lengths = length_of_strings(string_list)
    sum = 0
    
    for num in string_lengths:
        sum += num
        
    return num / len(string_lengths)

def main():
    print("Hello World!")
    test = mean_length_of_strings(["haha", "hrhrh", "hehea"])
    print(test)

if __name__ == "__main__":
    main()