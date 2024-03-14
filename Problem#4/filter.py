'''
name: Emma Verdugo
lab: @2pm
'''

def process_and_print(input_string):
    # Split into separate strings
    nums = input_string.split()

    # Convert strings to integers and filter out negative values
    input_data = [int(x) for x in nums]
    for x in input_data:
      if x >= 0:
        input_data.remove(x)
    # Sort integers in reverse order
    input_data.sort(reverse=True)
    # Print sorted integers
    for data in input_data:
      print(str(data)+" ",end="")
    #print( input_data )
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
