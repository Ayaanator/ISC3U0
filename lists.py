'''Learning lists'''

# Generate a list of integers from 1 to 10 using a for loop.
# Change all even numbers to have a negative sign in the previous list.
# Make a list of squares from 1 to 100 using a for loop.
# Print only odd squares from list above.
# Find the sum of all the items in the list. (Don't use sum() yet!)
# Okay, now use sum().

def main():
    my_list = []
    squares_list = []
    total = 0
    
    for i in range(10):
        my_list.append(i + 1)
        
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] *= -1
            
    print(my_list)
            
    for n in my_list:
        squared = n**2
        squares_list.append(squared)
        total += squared
        
    for num in squares_list:
        if num % 2 != 0:
            print(num, end=", ")
    

    print("\n" + str(total))
    print(sum(squares_list))
    
if __name__ == "__main__":
    main()