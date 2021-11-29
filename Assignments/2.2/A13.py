inp = input('Enter a sentence: ')  # Gets the users input
inplist = inp.split()  # Makes each word of the users input a different value in a list
for x in inplist:  # Iterates the following code for each value in the list
    # Prints the inverse of the current value of the list, and prints the next statement on the same line
    print(x[::-1], end=' ')