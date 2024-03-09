'''
name: Emma Verdugo
lab:@2pm

'''

def process_user_contacts(user_input):
    user_contacts = {} 
    
    user_input = user_input.replace(","," ")
    print(user_input)
    
    tokens = user_input.split(" ")
    print(tokens)
    
    # Put word pairs into a dictionary
    for i in range(0, len(tokens),2):
        contact_name = tokens[i]
        number = tokens[i + 1]
        
        user_contacts[contact_name] = number
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(user_contacts[contact_name])
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
