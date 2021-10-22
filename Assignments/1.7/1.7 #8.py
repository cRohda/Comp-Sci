for x in range(1, 4):  # repeat the loop for each number 1-3 (3 rows)
    counter = 0  # Sets counter to 0, this counts up for how many stars are in the row
    # loops through for the numbers 1-(4-x), x is the row, and there are less blank spaces in the higher numbered rows
    # so it will loop less for those rows
    for blank in range(1, 4-x):
        print(end='  ')  # prints the blank space before the stars
    # Loops while counter (set to 0 starting the loop) doesn't equal the equation
    while counter != (2 * x - 1):  # the equation multiplies the row by 2 (1 is top, 3 is bottom), and subtracts 1, so
        # for row 1 it would only print 1, but for row 3, it would print 5. this determines how many stars are printed
        print('* ', end='')  # prints the star (with space) and doesn't start a new line
        counter += 1  # adds one to the counter, so that stars stop printing at the right time
    print()  # Prints nothing to start a new line
