rows = int(input('How many rows should the rectangle have? '))  # Record the number of rows the user wants
columns = int(input('How many columns should the rectangle have? '))  # Records the number of columns the user wants

for x in range(columns):  # Run this code for how many columns the user entered
    for y in range(rows):  # Run this code for how many rows the user entered
        print('*', end='')  # for each row print *, and print the next one in the same row
    print()  # print nothing, creates a new row
