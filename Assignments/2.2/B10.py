a = True  # Creates a variable set to true
while a:  # While this variable is true, loop. Used to handle for 2+ word inputs
    inp = input('Enter ONE word: ')  # Takes the users input
    test = inp.split()  # Makes the users input a list of each word, to check how many words are there
    if len(test) == 1:  # If this list has 1 value, then it is only one word, so:
        a = False  # Set a to false so it ends the loop
        print(inp[::-1])  # Print the reverse of the string [{Beginning}:{End}:-1(Reverse)]
    else:  # If the list does not have 1 value (0 or 2+) then the input is invalid, so:
        # Ask the user to make a new input, and loop through again.
        print('Your input was either 2 words, or nothing at all. Please try again :)')