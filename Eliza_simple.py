# Eliza Application (simple)
# Kiran Pandey April 10, 2019
""" Eliza, a thearapist,
    is an interactive chat-bot that aks the user about a problem,
    evaluates the user response and
    interacts in a caring way
"""

# prompt the user about a problem
def ask(prompt):
    response = ask("What brings you in today? ")
    user_resp = input('Enter your response here or Q to quit: ')
    return user_resp

#interact in a caring way
def interact (user_resp):
    print (user_resp)

#executable program starts here

# initialize
done = False
exit = ['Q', 'I AM FEELING GREAT']
print ('Good day. I am Eliza. Your therapist for today. What brings you in today? ')

# loop through until user wants to quit
while not(done):
    user_resp = input('Enter your response here or Q to quit: ')
    if user_resp.upper() in exit:
        done = True
    else:
        interact(user_resp)


