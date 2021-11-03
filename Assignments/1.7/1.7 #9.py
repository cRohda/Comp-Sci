rows = int(input("Enter a row count: "))  # Gets user input for number of rows
for x in range(1, rows + 1):  # Loops through the number of times the use selected, starts at 1 to avoid crash if the
    # User inputs zero
    num = 1  # Sets the number to print as 1, the first number in the triangle
    print(" " * (rows - x), end="")  # Prints the amount of spaces in front of each row, decreases as row goes down
    # multiplies the space by rows user entered and the row its on, to make less lower.
    for y in range(1, x + 1):  # Loops through to print the numbers in each line
        print(num, end=" ")  # Outputs the current number to print
        num = num * (x - y) // y  # Pascal's triangle formula to determine the number to print
    print()  # Create a new line for the triangle