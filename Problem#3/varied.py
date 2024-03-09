'''
name: Emma Verdugo
lab: @2pm

'''

def process_input(input_string):
    # Split into separate strings
    num = input_string.split()
    # Convert strings to floats
    num = [float(x) for x in num]
    # Get max and average
    num = [ x for x in num if x>=0]
    max_value = max(num)
    average_value = sum(num) / len(num)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
