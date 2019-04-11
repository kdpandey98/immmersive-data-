# Magic-8Ball
# Kiran Pandey April 11, 2019
""" The Magic 8 Ball is a toy used for fortune-telling or seeking advice,
    developed in the 1950s and manufactured by Mattel.
    The user asks a yes-no question to the large plastic ball,
    then turns it over to reveal a (random) written answer
     which appears on the surface of the toy.
"""
# libraries used
import random

def get_response(user_resp):
    ''' function determines Magin 8ball's response randomly.
        set of responses predefined within the function
    '''
    # prededefined set of responses
    response = ['It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful']

    return (random.choice(response)) #   random response

# executable program starts here

# initialize
done = False
exit = ['no', 'n']      # condition to exit our of program
print ('Good day.')

# loop through until user wants to quit
while not(done):
    user_says = input('\nDo you have a question for the Magic 8-ball? respond "no" to quit: ').lower()
    print ('YOU ASKED: ',user_says)
    if user_says.lower() in exit:       # check if valid exit conditions update while loop condition
        done = True
        print ('Magic 8-Ball says: Thank you for playing!')
    else:
        print ('MAGIC 8-BALL SAYS: ', get_response(user_says))

