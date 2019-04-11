# Eliza Application (Full)
# Kiran Pandey April 10, 2019
""" Eliza, a thearapist,
    is an interactive chat-bot that aks the user about his/her problem,
    evaluates the user response and
    responds in a caring way (with hedges, qualifiers and replacement words)
"""
# libraries used
import random

#interact in a caring way
def get_response (user_resp):
    ''' function determines Eliza's response randomly hedge or prepend qualifier with replacement words.
        set of quailifiers and hedges are predefined within the function
    '''
# prededefined sets qulifiers, hedges and dictionary of substitute words
    resp_dict = {'i':'you','me':'you','my':'your','am':'are'}
    qualifier = ['Why do you say that',
                 'You seem to think that',
                 'So, you are concerned that']
    hedge = ['Please tell me more',
             'Many of my patients tell me the same thing',
             'It is getting late, maybe we had better quit']

#   random selection between hedge and qualifier with modification
    if random.randrange(2)==1:
        return(random.choice(hedge))
    else:
        response=[]      #if qualifier start with random qualifier
        response.append(random.choice(qualifier))

        words = user_resp.split()    # split user response to list to process each word separately
        for word in words:       # check each word in each user response; replace if in dictionary
            if word in resp_dict.keys():
                response.append(resp_dict[word])
            else:
                response.append(word)
        return ' '.join(response)    # convert list to a concatenated string

#executable program starts here

# initialize
done = False     # flag to check
exit = ['q', 'i am feeling great']    # condition to exit our of program
print ('Eliza: Good day. I am Eliza, your therapist. What brings you in today? ')

# loop through until user wants to quit
while not(done):
    user_says = input('\nEnter your response here or "Q" to quit: ').lower()
    print ('user: ',user_says)
    if user_says.lower() != 'q':        # check if user wants to quit
        print ('Eliza:', get_response(user_says))
    if user_says.lower() in exit:       # check if valid exit conditions update while loop condition
        done = True
        print ('Eliza: Thank you for stopping by. See you next time.')


