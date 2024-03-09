'''
name: Emma Verdugo
lab: @2pm

'''
def check_palindrome(user_input):
 #type your code here
 no_spaces = user_input.replace(" ","")
 rev = ''.join(reversed(no_spaces))

 if rev == no_spaces:
     print("palindrome: " + str(user_input))
 else:
     print("not a palindrome: " + str(user_input))
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
