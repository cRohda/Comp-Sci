again = 1  # Sets again to 1, for play again functionality
notInt = 1  # Sets notInt to 1, for error handling

while again == 1:  # Loop this as long as the player wants to play again
    while notInt == 1:  # Loop this as long as the player doesn't enter an integer
        try:  # Error handling to prevent crash if a non-int is entered
            inp = int(input('\nEnter a Number: '))  # Takes the users input and converts to int
            sqrt = inp ** 0.5  # takes the square root of the input
            if sqrt % 1 == 0:  # if the square root is a whole number
                print(f'Number is a perfect square ({sqrt})')  # print that the number is a perfect square, and what
                # the square is
            else:  # if it isn't
                print('Number is not a perfect square')  # Print that it isn't a perfect square
            Recon = 1  # sets recon to 1, for error handling on play again function
            while Recon == 1:  # Loop as long as Recon is 1, when the player enters not y/n
                askAgain = input('Would you like to try again? (y/n): ')  # ask if they want to play again
                if askAgain.lower() == 'y':  # if they want to play again
                    Recon = 0  # reset recon (ends loop)
                elif askAgain.lower() == 'n':  # If the user doesn't want to play again
                    Recon = 0  # end loop
                    again = 0  # end loop
                    notInt = 0  # end loop
                else:  # If the response is not y/n
                    print('Unrecognized Response')  # say that it is unrecognized, and loop to ask again
        except ValueError:  # if the number isn't an int
            print('Please Enter a number')  # ask to input an int, and loop again.
