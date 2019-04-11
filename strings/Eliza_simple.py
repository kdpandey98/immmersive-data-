# Eliza Application (simple)
# Kiran Pandey April 10, 2019
""" Eliza, a thearapist,
    is an interactive chat-bot that aks the user about a problem,
    evaluates the user response and
    interacts in a caring way (response is unchanged == user response )
"""

#interact in a caring way
def get_response (user_resp):
    ''' function determines Eliza's response with replacement words. '''
    return(user_resp)

#executable program starts here

# initialize
done = False
exit = ['q', 'i am feeling great']      # condition to exit our of program
print ('Good day. I am Eliza. Your therapist for today. What brings you in today? ')

# loop through until user wants to quit
while not(done):
    user_says = input('Enter your response here or "Q" to quit: ').lower()
    print ('user: ',user_says)
    if user_says.lower() != 'q':       # check if user wants to quit
        print ('Eliza:', get_response(user_says))
    if user_says.lower() in exit:       # check if valid exit conditions update while loop condition
        done = True
        print ('Eliza: Thank you for stopping by. See you next time.')