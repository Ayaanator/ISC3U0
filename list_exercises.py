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
    '''Returns a list of lengths of the each item in the string list'''
    result = []
    
    for i in range(len(string_list)):
        result.append(len(string_list[i]))
        
    return result

def mean_length_of_strings(string_list):
    '''Calculates the average length of all the words in a string list'''

    string_lengths = length_of_strings(string_list)
    sum = 0
    
    for num in string_lengths:
        sum += num
        
    return num / len(string_lengths)

def count(lst, item):
    '''Checks to see how many times a selected character appears in a string'''

    counter = 0
    
    for n in lst:
        if n == item:
            counter += 1
            
    return counter

def median(num_list):
    '''Returns the median number in a list'''

    num_list.sort()
    n = len(num_list)
    m = n // 2
    if n % 2 == 0:
        return (num_list[m - 1] + num_list[m]) / 2
    else:
        return num_list[m]
    
def median_length_of_strings(string_list):
    '''Returns hte median length in a string list'''
    return median(length_of_strings(string_list))

def parallel_lists(stdns, ids):

    print("CLASS LIST\n" + "-"*10)
    print("{:{width}}" .format("Student", width=15), end="")
    print("ID")
    for i in range (len(stdns)):
        print("{:{width}}".format(stdns[i], width=15), end="")
        print(ids[i])

def main():
    students = ["Arthur M", "Dutch V", "John M", "Sadie A", "Micah B"]
    student_ids = {"26734", "12569", "46882", "09869", "57425"}

    parallel_lists(students, student_ids)

if __name__ == "__main__":
    main()