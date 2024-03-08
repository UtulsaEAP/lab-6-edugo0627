'''
Name: Emma Verdugo
lab: @2pm Thursday

'''
def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    word = (tokens[0])
    num = (tokens[1])
    
    while word != 'quit':
       print( "Eating " + num +" " + word + " a day keeps you happy and healthy.")
       user_input = input()
       tokens = user_input.split()
       word = (tokens[0])
       num = (tokens[1])
if __name__ == "__main__":
    food_input()
