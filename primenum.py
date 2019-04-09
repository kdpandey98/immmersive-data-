# prime number
# Kiran Pandey April 8, 2019

# get inputs
num = int(input("What is your number: "))
print ('Numbers less than ', num, 'that are prime or not prime:')

# create placeholder for running list of primes, initialize to none
primes = []
print (1,' is not a prime number')  # 1 does not have two factors


for cur in range(2,num+1):  # loop through each number starting at 2 to determine if prime
    prime=True
    for den in primes: # determine if currnet number is divisible by any of previously identified primes
        if not (cur % den):
            print (cur,' is not a prime number')
            prime=False # if current is divisible end search 
            break
    if prime==True:  # all smaller primes have been tested so there are no smaller divisors
        print (cur, 'is a prime number')
        primes.append(cur) # add new prime to running list
print('and primes as a list ',primes)
