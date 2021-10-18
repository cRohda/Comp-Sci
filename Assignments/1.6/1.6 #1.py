start = 1  # Assigns Start to 1
Total = 0  # Assigns Total to 0
redo = 1  # Assigns redo to 1

while redo == 1:  # Loops while redo is = to 1
    try:  # Try statement to re-input if a non-int is entered
        End = int(input('Choose a Number: '))  # Asks for the input number
        redo = 0  # If the value is an int, redo is set to 0 to end the loop for if End is not an int
        while start <= End:  # Loops to add the numbers together, while Start is less than or equal to End
            Total = Total + start  # Equation to add the numbers
            start += 1  # Adds 1 to start for each number
    except ValueError:  # Exception for a non-int input
        print('Your input was not a number')  # Prints for the user to re-enter their input

print(f'The total is {Total}')  # Prints the total value
