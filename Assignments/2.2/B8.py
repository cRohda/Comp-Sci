word = "incredible"  # Create the string to look in

inp = input('Enter a letter: ')  # Take the users input of a letter

if inp in word:  # If the users letter is in the string
    print('The letter you guessed is in' + word)  # Print that it is in
else:  # Else
    print('The letter you guessed is not in ' + word)  # Print that it is not in