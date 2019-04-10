# Collatz Sequence
# Kiran Pandey April 8, 2019

# get inputs 
num = int(input('What is your input?'))
output = [num]
iter = 1000    # counter to exit if no solution 

while num > 1:   # exit condition when num reaches 1 (also traps fractions)
    if not (num % 2):
        num = int(num / 2)
        print (output)
    else:
        num = num * 3 + 1
        print (output)
    output.append(num)    
print (output)

