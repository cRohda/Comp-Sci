loop = 1  # Sets loop to 1 (for error handling, when user enters a non-int)
x = 0  # Sets x to 0, to count up through all possible numbers
total = 0  # Sets total to 0, to count up through the number of divisors

while loop == 1:  # Loop while loop is 1, used to re-ask for number when a non-int is entered
    try:  # Try this code, used for error handling
        inp = int(input('Enter a number: '))  # Asks for users input and makes it an int
        while x < inp:  # loop while the value of x is less than the input
            x += 1  # add 1 to x
            if inp % x == 0:  # if the input is evenly divisible by the new value of x
                total += 1  # add 1 to the total number of divisors
            else:  # if it isn't evenly divisible
                pass  # do nothing

        if total == 2:  # if the total number of divisors is 2 (1 and itself)
            print(f'\n{inp} is a prime number!')  # the number is prime, print that it is prime (and make a new line)
            break  # end the loop
        else:  # if there are more than 2 divisors (not prime)
            print(f'\n{inp} is not a prime number, it has {total} divisors\n')
            x = 0
            while x < inp:  # loop while the value of x is less than the input
                x += 1  # add 1 to x
                if inp % x == 0:  # if the input is evenly divisible by the new value of x
                    print(f'{inp} is divisible by {x}')  # print the number it is divisible by
                    total += 1  # add 1 to the total number of divisors
                else:  # if it isn't evenly divisible
                    pass  # do nothing
            # print that it isn't prime, and how many
            # divisors it has
            break  # end the loop
    except ValueError:  # if there is a value error
        print('Please enter a number')  # print to enter a number, and re-ask
