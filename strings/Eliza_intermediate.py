# Eliza Application (intermediate)
# Kiran Pandey April 10, 2019
""" Eliza, a thearapist,
    is an interactive chat-bot that aks the user about his/her problem,
    evaluates the user response and
    responds in a caring way (with replacement words for specific words)
"""

#interact in a caring way
def get_response (user_resp):
    ''' function determines Eliza's response with replacement words. '''
    # prededefined dictionary of substitute words
    resp_dict = {'i':'you','me':'you','my':'your','am':'are'}

    words = user_resp.split()   # split user response to list to process each word separately

    response=[]   # initialize response as empty list to append words
    for word in words:   # check each word in each user response; replace if in dictionary
        if word in resp_dict.keys():
            response.append(resp_dict[word])
        else:
            response.append(word)
    return ' '.join(response)   # convert list to a concatenated string

#executable program starts here

# initialize
done = False
exit = ['q', 'i am feeling great']  # condition to exit our of program
print ('Eliza: Good day. I am Eliza, your therapist. What brings you in today? ')

# loop through until user wants to quit
while not(done):
    user_says = input('Enter your response here or "Q" to quit: ').lower()
    print ('user: ',user_says)
    if user_says.lower() != 'q':       # check if user wants to quit
        print ('Eliza:', get_response(user_says))
    if user_says.lower() in exit:       # check if valid exit conditions update while loop condition
        done = True
        print ('Eliza: Thank you for stopping by. See you next time.')


