x = 99  # Assigns X to 100 (To make the count start with 3 digit numbers0
total = 0  # Sets the total to 0 (Counts the number of matches)
inp = int(input('Enter a number: '))  # Takes the users input for the number
while x <= 998:  # Counts until it has tried all numbers 100-999
    x += 1  # Adds one to the number to try
    if x % inp == 0:  # If the number is divisible by the input
        print(x)  # Print the number that works
        total += 1  # Add one to the total number of matches
    else:  # If the number doesnt work
        pass  # Do nothing
print(f'There were {total} matches')  # Prints the total number of matches
