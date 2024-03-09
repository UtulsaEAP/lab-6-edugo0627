'''
name: Emma Verdugo
lab:@2pm

'''

def filter_and_print_range(input_list, min_val, max_val):
    #write your code here

     for x in input_list:
        if min_val < x < max_val:
            print(x)

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(x) for x in user_input]
    input_list = integer_list.split(" ")

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = user_input.split(" ")
    
    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(input_list, min_val, max_val)
