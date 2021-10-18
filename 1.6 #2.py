redo = 1  # Sets redo to 1 (for the user not entering an int)
index = 1  # Sets index to 1 (Counter for how many numbers entered)
total = 0  # Sets total to 0 (For total value of inputs)
while redo == 1:  # Loops while redo is 1, for if the user enters not an int
    try:  # Error handlingR
        while (index <= 10):  # Loops 10 times
            inp = int(input('Enter a number: '))  # takes users input for the numbers
            total = total + inp  # Adds the new number to the total
            index += 1  # Sets the counter up one (to count 10 inputs)
        redo = 0  # Sets redo to 0, to end the re-input for a non-int
    except ValueError:  # Error handling
        print('You did not enter an int')  # Prints a statement if the user enters a non-int
print(f'the average is {total/10}')  # Prints the average
